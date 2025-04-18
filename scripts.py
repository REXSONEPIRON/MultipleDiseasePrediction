#import necessary libraries
import psycopg2 # Used to connect and interact with PostgreSQL databases
from tabulate import tabulate # Used to display tabular data
from datetime import datetime # Used to work with date and time
import pandas as pd 

# Defining the class for Agent Policy Rankings
class AgentPolicyRankings:
    def __init__(self):
         # Database connection parameters for PLSQL
        self.db_params = {
            'dbname': 'submission_tracking_db',
            'user': '',
            'password': '',
            'host': '',
            'port': '5432'# Default port for PostgreSQL
        }
        
# Method to format date values

    def format_date(self, date_value):
        if pd.isna(date_value):#used to detect missing values
            return ''
        try:  # Convert date to a specific string format
            return pd.to_datetime(date_value).strftime('%Y-%m-%d %H:%M:%S')#is used to convert a date value into a specific date format using Pandas
        except:
            return str(date_value)# Return as string if conversion fails

    def get_rankings(self, start_date='2025-01-27', end_date='2025-02-07'):# Method to get agent rankings from the database
       
       # SQL query using TABLES to get policy data  
        query = """
        WITH base_policies AS (
            SELECT DISTINCT ON (l.first_name, l.last_name)
                p.policy_id,
                p.agent_id,
                p.date_created,
                p.premium_actual,
                pr.category_id,
                pr.name as product_name,
                pc.name as category_name,
                c.name as carrier_name,
                LOWER(TRIM(l.first_name)) as first_name,
                LOWER(TRIM(l.last_name)) as last_name,
                LOWER(TRIM(l.state)) as state,
                psh.status_name
            FROM policies p
            JOIN policy_status_history psh ON p.policy_id = psh.policy_id
            JOIN products pr ON p.product_id = pr.product_id
            JOIN product_categories pc ON pr.category_id = pc.category_id
            JOIN carriers c ON pr.carrier_id = c.carrier_id
            JOIN leads l ON p.lead_id = l.lead_id
            WHERE 
                pr.category_id = 1
                AND p.date_created BETWEEN %s AND %s::timestamp + interval '23 hours 59 minutes 59 seconds'
                AND psh.status_name IN ('2025_active', 'active')
            ORDER BY l.first_name, l.last_name, p.date_created
        ),
        agent_stats AS (
            SELECT 
                bp.agent_id,
                COUNT(*) as total_policies,
                COUNT(*) as unique_policies,
                SUM(bp.premium_actual) as total_premium,
                STRING_AGG(DISTINCT bp.carrier_name, ', ') as carriers
            FROM base_policies bp
            GROUP BY bp.agent_id
        )
        SELECT 
            a.agent_id,
            a.full_name as agent_name,
            a.email as agent_email,
            COALESCE(ast.total_policies, 0) as total_policies,
            COALESCE(ast.unique_policies, 0) as unique_policies,
            COALESCE(ast.total_policies, 0) as converted_policies,
            COALESCE(ast.unique_policies, 0) as unique_converted_policies,
            COALESCE(ast.total_premium, 0) as total_premium,
            COALESCE(ast.carriers, '') as carriers,
            100 as conversion_rate
        FROM agents a
        LEFT JOIN agent_stats ast ON a.agent_id = ast.agent_id
        WHERE ast.unique_policies > 0
        ORDER BY ast.unique_policies DESC, ast.total_premium DESC;
        """
        
        try:# Connecting to PostgreSQL and executing the query
            with psycopg2.connect(**self.db_params) as conn:
                # Executing the query and returning the result as a DataFrame
                return pd.read_sql(query, conn, params=(
                    start_date,
                    end_date
                ))
        except Exception as e:
            print(f"Error executing query: {e}")# Print the error if query fails
            raise #raise statement is used to manually trigger an exception. This is useful when you want to indicate that an error has occurred

# Method to generate an Excel report for agent rankings
    def generate_report(self, start_date='2025-01-27', end_date='2025-02-07'):
        try:
            # Get the summary rankings
            df_summary = self.get_rankings(start_date, end_date)
            
            # Create the summary rankings sheet - FIXED COLUMN ORDER
            df_summary['Rank'] = range(1, len(df_summary) + 1)
            
            # Explicitly define summary columns and their order
            display_columns = [
                'Rank',
                'agent_name',
                'total_policies',
                'unique_policies',
                'converted_policies',
                'unique_converted_policies',
                'conversion_rate',
                'total_premium',
                'carriers',
                'agent_id',
                'agent_email'
            ]
            # Renaming columns for better readability
            column_names = {
                'agent_name': 'Agent Name',
                'total_policies': 'Raw Policies',
                'unique_policies': 'Unique Policies',
                'converted_policies': 'Total Conversions',
                'unique_converted_policies': 'Unique Conversions',
                'conversion_rate': 'Conv. Rate %',
                'total_premium': 'Total Premium',
                'carriers': 'Carriers',
                'agent_id': 'Agent ID',
                'agent_email': 'Email'
            }
            
            # Create summary dataframe with correct columns
            display_df = df_summary[display_columns].rename(columns=column_names)
            
            # Get raw data
            raw_query = """
            SELECT DISTINCT ON (l.first_name, l.last_name)
                p.policy_id,
                p.lead_id,
                COALESCE(p.agent_id, 0) as agent_id,
                COALESCE(a.full_name, 'Unknown Agent') as agent_name,
                p.date_created::text as date_created,
                p.premium_actual,
                pr.category_id,
                pr.name as product_name,
                pc.name as category_name,
                c.name as carrier_name,
                LOWER(TRIM(l.first_name)) as first_name,
                LOWER(TRIM(l.last_name)) as last_name,
                LOWER(TRIM(l.state)) as state,
                psh.status_name,
                psh.disposition_type,
                psh.created_at::text as status_date,
                CONCAT(LOWER(TRIM(l.first_name)), '|', LOWER(TRIM(l.last_name)), '|', LOWER(TRIM(l.state))) as unique_identifier
            FROM policies p
            JOIN policy_status_history psh ON p.policy_id = psh.policy_id
            JOIN products pr ON p.product_id = pr.product_id
            JOIN product_categories pc ON pr.category_id = pc.category_id
            JOIN carriers c ON pr.carrier_id = c.carrier_id
            JOIN leads l ON p.lead_id = l.lead_id
            LEFT JOIN agents a ON p.agent_id = a.agent_id
            WHERE 
                pr.category_id = 1
                AND p.date_created BETWEEN %s AND %s::timestamp + interval '23 hours 59 minutes 59 seconds'
                AND psh.status_name IN ('2025_active', 'active')
            ORDER BY l.first_name, l.last_name, p.date_created
            """

               # Connecting to PostgreSQL using connection parameters
            with psycopg2.connect(**self.db_params) as conn:
                df_raw = pd.read_sql(raw_query, conn, params=(start_date, end_date))
            
            # Format currencies
            display_df['Total Premium'] = display_df['Total Premium'].apply(
                lambda x: f"${x:,.2f}" if pd.notnull(x) else '' #, adds commas as thousands separators.,.2f ensures the number has two decimal places.,$ adds the dollar sign at the beginning.
            )
            
            df_raw['premium_actual'] = df_raw['premium_actual'].apply(
                lambda x: f"${x:,.2f}" if pd.notnull(x) else ''
            )
            
            # Create Excel writer object
            filename = f"agent_rankings_detailed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                # Write summary sheet with correct columns
                display_df.to_excel(writer, sheet_name='Rankings Summary', index=False)
                
                # Write all raw data
                df_raw.to_excel(writer, sheet_name='All Raw Data', index=False)
                
                # Write individual agent sheets with better naming
                for agent_id in df_raw['agent_id'].unique():
                    agent_name = df_raw[df_raw['agent_id'] == agent_id]['agent_name'].iloc[0]#.iloc is used to access rows by index position.0 means it access the first element
                    agent_data = df_raw[df_raw['agent_id'] == agent_id]
                    # Create sheet name with agent name and ID
                    sheet_name = f'{agent_name} ({agent_id})'[:31]  # Excel limit is 31 chars
                    agent_data.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Get workbook and worksheet objects
                workbook = writer.book
                
                # Add formats
                header_format = workbook.add_format({
                    'bold': True,
                    'bg_color': '#D3D3D3',
                    'border': 1
                })
                
                # Format all sheets
                for sheet_name in writer.sheets:
                    worksheet = writer.sheets[sheet_name]
                    # Get the appropriate dataframe for this sheet
                    if sheet_name == 'Rankings Summary':
                        df = display_df
                    else:
                        df = df_raw
                    
                    # Format headers
                    for col_num, value in enumerate(df.columns.values):
                        worksheet.write(0, col_num, value, header_format)
                    
                    # Adjust column widths
                    for idx, col in enumerate(df.columns):
                        # Get the maximum length of the column content
                        max_length = max(
                            df[col].astype(str).apply(len).max(),
                            len(str(col))
                        ) + 2  # Add a little extra space
                        worksheet.set_column(idx, idx, max_length)
            
            # Print report to console
            print("\n=== Complete Agent Policy Rankings (Using Status History) ===")
            print(f"Period: {start_date} to {end_date} (inclusive)")
            print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\nNotes:")
            print("- Rankings based on unique converted policies")
            print("- Conversions counted if policy ever had a sale status")
            print("- 'Unique Policies' counts distinct individuals by name/state")
            print("- Date range includes full days (00:00:00 to 23:59:59)")
            print(f"\nDetailed report exported to: {filename}")
            print("\nReport includes:")
            print("1. Rankings Summary")
            print("2. All Raw Policy Data")
            print("3. Individual sheets for each agent's policies")
            
            print("\nSummary Statistics:")
            print(f"Total Agents with Policies: {len(df_summary)}")
            print(f"Total Raw Policies: {df_summary['total_policies'].sum():,}")
            print(f"Total Unique Policies: {df_summary['unique_policies'].sum():,}")
            print(f"Total Converted Policies: {df_summary['converted_policies'].sum():,}")
            print(f"Total Unique Conversions: {df_summary['unique_converted_policies'].sum():,}")
            print(f"Average Conversion Rate: {df_summary['conversion_rate'].mean():.2f}%")
            print(f"Total Premium: ${df_summary['total_premium'].sum():,.2f}")
            
            return {
                'summary': display_df,
                'raw_data': df_raw
            }
                
        except Exception as e:
            print(f"Error generating report: {e}")
            raise


def main():
    try:
           # Creating an instance of the class
        rankings = AgentPolicyRankings()
        # Generating the report for the specified date range
        rankings.generate_report('2025-01-27', '2025-02-07')
    except Exception as e:
        print(f"Error running rankings report: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
