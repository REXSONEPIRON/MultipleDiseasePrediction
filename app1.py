import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
import pickle as pkl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return email_regex#email.endswith('@gmail.com')

#model = pkl.load(open('cancer.pkl','rb'))
st.set_page_config(page_title='Medipredict - Disease Prediction System',page_icon = 'hospital',layout= 'wide')

# st.title('Lung Cancer Prediction')  
#df = pd.read_csv('survey lung cancer.csv')

#model1 = pkl.load(open('Heart.pkl','rb'))
#df1 = pd.read_csv('cardiotrain.csv')

with st.sidebar:
    selected = option_menu(menu_title= 'Main Menu',
                           options= ['Home','Lung Cancer Prediction','Cardiovascular Disease prediction','Diabetes Prediction','About us'],
                           icons = ['house','lungs','heart','🩸','info-circle-fill'],
                           menu_icon='cast',
                           styles={
                         # "container": {"padding": "5!important","background-color":'white'},
                           "icon": {"color": "white", "font-size": "23px"}, 
                           "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#c970d8"},
                           "nav-link-selected": {"background-color": "#e9232f"},
                               } 
            
    )
#---------------------------------------------------------
if selected == 'Home':
  diabetes_img = Image.open("diabetes.jpg")  
   #diabetes_img = Image.open("diabetes.png") 
  heart_img = Image.open("heart.png")  
  lung_img = Image.open("Lung Cancer.jpg") 

# Centered title with box styling
  st.markdown('<div class="main-title">MULTIPLE DISEASE PREDICTION SYSTEM</div>', unsafe_allow_html=True)
  st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(90deg, #e100ff, #7f00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 2s ease-in-out;
        margin-bottom: 10px;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #444;
        font-family: 'Segoe UI', sans-serif;
        padding: 0px 100px;
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .card-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 50px;
        flex-wrap: wrap;
    }

    .card {
        background-color: #ffffff;
        border-radius: 20px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        width: 300px;
        overflow: hidden;
        text-align: center;
    }

    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 12px 30px rgba(0, 0, 0, 0.2);
    }

    .card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-bottom: 1px solid #eee;
    }

    .card-title {
        font-size: 20px;
        font-weight: 600;
        margin: 15px 0 25px 0;
        color: #333;
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
# Paragraph explaining the app
  st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-size:18px;'>
        This Web Application is designed to help users predict the likelihood of developing certain diseases based on their input features.
        With the use of trained and tested machine learning models, we provide predictions for
        <span class="highlight">Lung Cancer</span>, <span class="highlight">Cardiovascular Disease prediction</span> and <span class="highlight">Diabetes Prediction</span>.</div>""", unsafe_allow_html=True)
    

# Display three disease prediction icons with labels
  st.markdown("""
    <style>
    .img-hover-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 30px;
    }

    .hover-box {
        border-radius: 20px;
        overflow: hidden;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        width: 300px;
        text-align: center;
        background-color: #fff;
    }

    .hover-box:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }

    .caption {
        margin-top: 10px;
        font-size: 18px;
        font-weight: 600;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Create 3 columns for layout

  col1, col2, col3 = st.columns(3)

  with col3:
    st.markdown('<div class="hover-box">', unsafe_allow_html=True)
    st.image(diabetes_img, width=240)
    st.markdown('<div class="caption">Diabetes Prediction</div></div>', unsafe_allow_html=True)

  with col2:
    st.markdown('<div class="hover-box">', unsafe_allow_html=True)
    st.image(heart_img, width=240)
    st.markdown('<div class="caption">Cardiovascular Disease prediction</div></div>', unsafe_allow_html=True)

  with col1:
    st.markdown('<div class="hover-box">', unsafe_allow_html=True)
    st.image(lung_img, width=240)
    st.markdown('<div class="caption">Lung Cancer Prediction</div></div>', unsafe_allow_html=True)
    
          # Inject custom CSS for background and text styling
  st.markdown("""
    <style>
    .main {
        background-image: url("images/background.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 50px;
        font-family: 'Segoe UI', sans-serif;
        color: #1c1c1c;
    }

    .section-title {
        font-size: 32px;
        font-weight: bold;
        color: #004d66;
        margin-bottom: 20px;
    }

    .sub-section {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    ul {
        margin-left: 20px;
    }

    .disclaimer {
        font-style: italic;
        color: #333;
    }

    .highlight {
        color: #ff4d4d;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Background wrapper
  st.markdown('<div class="main">', unsafe_allow_html=True)

# Section Title
  st.markdown('<div class="section-title">📘 User Guide & Disclaimer</div>', unsafe_allow_html=True)

# How to Use Section
  st.markdown("""
<div class="sub-section">
    <h4><b>🛠️ How to Use:</b></h4>
    <ul>
        <li>Navigate to the Main Menu (☰) on the top-left corner.</li>
        <li>Select a tab like <b>'Diabetes Prediction'</b>, <b>'Heart Disease'</b>, or <b>'Lung Cancer'</b>.</li>
        <li>Fill in the required health information accurately.</li>
        <li>Click the <b>"Test Result"</b> button to view your predictions.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Disclaimer Section
  st.markdown("""
<div class="sub-section">
    <h4><b>⚠️ Disclaimer:</b></h4>
    <ul class="disclaimer">
        <li>This app may not provide accurate predictions at all times.</li>
        <li>Please double-check your input and consult a medical expert if in doubt.</li>
        <li>Your information is used solely for test result communication and is kept confidential.</li>
        <li>Use this tool only for awareness. It is <span class="highlight">not a replacement for professional medical advice</span>.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Note Section (My suggestion)
  st.markdown("""
<div class="sub-section">
    <h4><b>💡 Note:</b></h4>
    <p>For any unusual symptoms or concerns, we strongly recommend scheduling a consultation with a certified healthcare provider for personalized diagnosis and treatment.</p>
</div>
""", unsafe_allow_html=True)

# Close main wrapper
  st.markdown('</div>', unsafe_allow_html=True)
  st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px;'>
        &copy; 2025 | Developed by Rexson Epiron
    </div>
    """,
    unsafe_allow_html=True
)
#---------------------------------------------------------------
if selected=='Lung Cancer Prediction':
    tab1, tab2 = st.tabs(["🫁 Lung Cancer Diagnosis", "📘 About Lung Cancer"])
    with tab1:
        model = pkl.load(open('cancer.pkl','rb'))
        df = pd.read_csv('survey lung cancer.csv')
        st.title('Lung Cancer Prediction')
        name = st.text_input("Name")
        email = st.text_input("Email")
        email_sender = 'noreplymedipredict@gmail.com'##rexsonepiron@gmail.com
        password = 'bcys ibmv qvla tbig' 
        st.warning('Please enter both Name and Email to proceed!') 

        if email:
            a1,a2,a3 = st.columns(3)
            
            with a1:
                Gender = st.selectbox('Select Your Gender',('Male','Female'))
                Age = st.number_input('Enter Your Age',18,87)
                Smoke = st.selectbox('Do you smoke?',('Yes','No'))
                Chronic_Disease = st.selectbox('Do you have any chronic diseases?',('Yes','No'))
            with a2:
                Fatigue = st.selectbox('Do you experience fatigue?',('Yes','No'))
                Wheezing = st.selectbox('Do you experience wheezing?',('Yes','No'))
                Alcohol_Consuming = st.selectbox('Do you consume alcohol?',('Yes','No'))
                Coughing = st.selectbox('Do you have a persistent cough?',('Yes','No'))
            with a3:
                Sortness_of_Breath = st.selectbox('Do you experience shortness of breath?',('Yes','No'))
                Swallowing = st.selectbox('Do you have difficulty swallowing?',('Yes','No'))
                Chest_pain = st.selectbox('Do you experience chest pain?',('Yes','No'))



            if a3.button('Lung Cancer Test Result'):
                input_data_module=pd.DataFrame(
                    [[Gender,Age,Smoke,Chronic_Disease,Fatigue,Wheezing,Alcohol_Consuming,Coughing,Sortness_of_Breath,Swallowing,Chest_pain]],
                    columns=['GENDER', 'AGE', 'SMOKING', 'CHRONIC DISEASE', 'FATIGUE ', 'WHEEZING',
            'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
            'SWALLOWING DIFFICULTY', 'CHEST PAIN']
                    )
            
                input_data_module['GENDER'].replace(['Male','Female'],[1,2],inplace=True)
                input_data_module['SMOKING'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['CHRONIC DISEASE'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['FATIGUE '].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['WHEEZING'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['ALCOHOL CONSUMING'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['COUGHING'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['SHORTNESS OF BREATH'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['SWALLOWING DIFFICULTY'].replace(['No','Yes'],[1,2],inplace=True)
                input_data_module['CHEST PAIN'].replace(['No','Yes'],[1,2],inplace=True)

                Lung_cancer_prediction = model.predict(input_data_module)
                
                row_wise_df = pd.DataFrame(input_data_module)#.transpose()
                if Lung_cancer_prediction == 1:
                    st.error('POSITIVE')
                     
                    
                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body = """<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App</p>
                                        <h2 style="color:#ff2b2b;">Lung Cancer Test Result: Positive</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Lung Cancer:</h2>
                                        <ul>
                                            <li><b>Avoid Smoking:</b> The most significant risk factor for lung cancer is smoking. Quitting smoking is the best preventive measure.</li>
                                            <li><b>Radon Exposure:</b> Test your home for radon, a naturally occurring gas that can contribute to lung cancer.</li>
                                            <li><b>Protect Against Workplace Carcinogens:</b> If you work in an industry with exposure to carcinogens, use protective equipment and follow safety guidelines.</li>
                                            <li><b>Healthy Diet:</b> Consume a diet rich in fruits and vegetables, which may have protective effects against certain cancers.</li>
                                            <li><b>Regular Exercise:</b> Engage in regular physical activity to maintain overall health.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Symptoms:</b> Be aware of symptoms like persistent cough, chest pain, and unexplained weight loss. Consult a healthcare professional if you experience these.</li>
                                            <li><b>Limit Alcohol Consumption:</b> If you consume alcohol, do so in moderation. Excessive alcohol intake is associated with an increased risk of various cancers, including lung cancer.</li>
                                            <li><b>Regular Health Check-ups:</b> Schedule regular check-ups with your healthcare provider for early detection of potential health issues, including lung cancer.</li>
                                            <li><b>Awareness and Education:</b> Stay informed about lung cancer risks and symptoms. Early awareness and seeking medical attention promptly can improve treatment outcomes.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩Email sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}")
                
                else:
                    st.success('NEGATIVE')
                    
                    
                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body ="""<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App!</p>
                                        <h2 style="color:#09ab3b;">Lung Cancer Test Result: Negative</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Lung Cancer:</h2>
                                        <ul>
                                            <li><b>Avoid Smoking:</b> The most significant risk factor for lung cancer is smoking. Quitting smoking is the best preventive measure.</li>
                                            <li><b>Radon Exposure:</b> Test your home for radon, a naturally occurring gas that can contribute to lung cancer.</li>
                                            <li><b>Protect Against Workplace Carcinogens:</b> If you work in an industry with exposure to carcinogens, use protective equipment and follow safety guidelines.</li>
                                            <li><b>Healthy Diet:</b> Consume a diet rich in fruits and vegetables, which may have protective effects against certain cancers.</li>
                                            <li><b>Regular Exercise:</b> Engage in regular physical activity to maintain overall health.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Symptoms:</b> Be aware of symptoms like persistent cough, chest pain, and unexplained weight loss. Consult a healthcare professional if you experience these.</li>
                                            <li><b>Limit Alcohol Consumption:</b> If you consume alcohol, do so in moderation. Excessive alcohol intake is associated with an increased risk of various cancers, including lung cancer.</li>
                                            <li><b>Regular Health Check-ups:</b> Schedule regular check-ups with your healthcare provider for early detection of potential health issues, including lung cancer.</li>
                                            <li><b>Awareness and Education:</b> Stay informed about lung cancer risks and symptoms. Early awareness and seeking medical attention promptly can improve treatment outcomes.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩mail sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}")
    with tab2:
        # Lung Cancer Info Section
        st.markdown("""
        ## 🫁 **All You Need to Know About Lung Cancer!**

        Lung cancer is a type of cancer that begins in the lungs — the two spongy organs in your chest that help you breathe. It is one of the leading causes of cancer deaths worldwide, but early detection can significantly improve treatment outcomes.

        ---

        ### 🔍 **What are the symptoms of lung cancer?**
        Lung cancer often doesn’t cause signs and symptoms in its early stages. When symptoms do occur, they may include:

        - Persistent cough that doesn’t go away
        - Chest pain that worsens with deep breathing, coughing, or laughing
        - Hoarseness or voice changes
        - Unexplained weight loss
        - Coughing up blood
        - Shortness of breath
        - Frequent respiratory infections like bronchitis or pneumonia
        - Feeling tired or weak

        ---

        ### ⚠️ **What are the risk factors for lung cancer?**
        Several risk factors can increase the likelihood of developing lung cancer, including:

        - **Smoking** – the leading cause of lung cancer
        - **Exposure to secondhand smoke**
        - **Prolonged exposure to radon gas**
        - **Asbestos or other environmental toxins**
        - **Family history of lung cancer**
        - **Air pollution**
        - **Radiation therapy to the chest**

        ---

        Early detection through regular screening and quitting smoking can dramatically reduce the risk and improve survival rates.
        """)
        st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px;'>
        &copy; 2025 | Developed by Rexson Epiron
    </div>
    """,
    unsafe_allow_html=True
)

#--------------------------------------------------------------------------------------------------
if selected=='Cardiovascular Disease prediction':
    #st.title("❤️ Cardiovascular Disease prediction")
    #st.markdown("### ❤️ Heart Diagnosis &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 📋 About Heart Disease", unsafe_allow_html=True)
    #st.markdown("---")
    tab11, tab12 = st.tabs(["❤️ Cardiovascular Disease prediction", "🗒️ About Cardiovascular Disease"])
    with tab11:
        model1 = pkl.load(open('Heart.pkl','rb'))
        df1 = pd.read_csv('cardio_1.csv')
        st.title('Cardiovascular Disease prediction')  
        name = st.text_input("Name")
        email = st.text_input("Email")
        email_sender = 'noreplymedipredict@gmail.com'##rexsonepiron@gmail.com
        password = 'bcys ibmv qvla tbig' 
        st.warning('Please enter both Name and Email to proceed!') 

        if email:
            a1,a2,a3 = st.columns(3)

            with a1:
                gender = st.selectbox('Select Your Gender',('Female','Male'))
                height = st.number_input('Enter your Height (in centimeters)',55,250)
                weight = st.number_input('Enter your Weight (in kilograms)',10,200)
                ap_hi = st.number_input('Enter your Systolic Blood Pressure level',90,180)
                #ap_hi = st.selectbox('Select your Systolic Blood Pressure level',('Normal ~ 90 to 120','Hypertension Stage 1 ~121 to 140','Hypertensive Crisis ~141 to 180'))
            with a2:
                ap_lo = st.number_input('Enter your Diastolic Blood Pressure level',60,120)
                #ap_lo = st.selectbox('Select your Diastolic Blood Pressure level',('Normal ~ 60 to 80','Hypertension Stage 1 ~81 to 99','Hypertensive Crisis ~100 or Above'))
                cholesterol = st.selectbox('Do you have cholesterol',('Normal','above normal','well above normal'))
                gluc = st.selectbox('Select your Glucose level',('Normal','above normal','well above normal'))
                smoke = st.selectbox('Do you smoke?',('Yes','No'))
            with a3:
                alco = st.selectbox('Do you consume alcohol?',('Yes','No'))
                Exact_Age = st.number_input('Enter Your Age',23,87)

            if a3.button('Cardiovascular Disease Test Result'):
                input_data = pd.DataFrame([[gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, Exact_Age]],
            columns=['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 
                    'gluc', 'smoke', 'alco', 'Exact_Age'])
            
                input_data['gender'].replace(['Female', 'Male'], [1, 2], inplace=True)
                #input_data['ap_hi'].replace(['Normal ~ 90 to 120', 'Hypertension Stage 1 ~121 to 140', 'Hypertensive Crisis ~141 to 180'], [1, 2, 3], inplace=True)
                #input_data['ap_lo'].replace(['Normal ~ 60 to 80', 'Hypertension Stage 1 ~81 to 99', 'Hypertensive Crisis ~100 or Above'], [1, 2, 3], inplace=True)
                input_data['cholesterol'].replace(['Normal', 'above normal', 'well above normal'], [1, 2, 3], inplace=True)
                input_data['gluc'].replace(['Normal', 'above normal', 'well above normal'], [1, 2, 3], inplace=True)
                input_data['smoke'].replace(['No', 'Yes'], [0, 1], inplace=True)
                input_data['alco'].replace(['No', 'Yes'], [0, 1], inplace=True)

                input_data = input_data[['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 
                                'cholesterol', 'gluc', 'smoke', 'alco', 'Exact_Age']]
                
                Cardiovascular_Disease_prediction = model1.predict(input_data)
                users_data = [height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco]
                row_wise_df1 = pd.DataFrame(input_data).transpose()
                if Cardiovascular_Disease_prediction == 1:
                    st.error('POSITIVE')
                    with st.expander("Click here to see Test Report", expanded=True):
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.markdown(f"**Patient Name:** {name}")
                        with c2:
                            st.markdown(f"**Gender:** {gender}")
                        with c3:
                            st.markdown(f"**Age:** {Exact_Age}")

                        parameters = ["Height", "Weight", "Systolic Blood Pressure (mmHg)", "Diastolic Blood Pressure (mmHg)","Cholesterol", "Glucose", "Smoking", "Alcohol Intake"]
                        normal_ranges = ["Greater Then 160 cm", "55-79 kg", "90-120 mmHg", "60-90 mmHg","Normal - Above Normal", "Normal", "No", "No"]   
                        df = pd.DataFrame({"Parameter Name": parameters,"Patient Values":users_data,"Normal Range": normal_ranges})
                        st.table(df.reset_index(drop=True))
                        st.info("ℹ️ Do check your email for more details, Thank You.")  

                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body = """<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App</p>
                                        <h2 style="color:#ff2b2b;">cardiovascular Disease Test Result: Positive</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Cardiovascular Disease Prevention:</h2>
                                        <ul>
                                            <li><b>Quit Smoking:</b> Smoking is a major risk factor for cardiovascular disease. Quitting smoking improves heart health and reduces the risk of heart attacks and strokes.</li>
                                            <li><b>Healthy Diet:</b> Consume a heart-healthy diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit salt, sugar, and saturated fat intake to maintain healthy cholesterol and blood pressure levels.</li>
                                            <li><b>Regular Exercise:</b> Engage in regular physical activity, such as walking, jogging, cycling, or swimming, for at least 30 minutes a day, most days of the week, to strengthen the heart and improve circulation.</li>
                                            <li><b>Maintain Healthy Weight:</b> Achieve and maintain a healthy weight to reduce the strain on the heart and lower the risk of hypertension and type 2 diabetes.</li>
                                            <li><b>Manage Stress:</b> Practice stress management techniques such as deep breathing, meditation, or yoga to reduce stress and its impact on heart health.</li>
                                            <li><b>Limit Alcohol Consumption:</b> Drink alcohol in moderation, if at all, as excessive alcohol intake can lead to high blood pressure, heart failure, and other cardiovascular problems.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Symptoms:</b> Be aware of cardiovascular symptoms such as chest pain, shortness of breath, irregular heartbeat, dizziness, and unexplained fatigue. Seek medical attention if you experience these symptoms.</li>
                                            <li><b>Regular Health Check-ups:</b> Schedule regular check-ups to monitor blood pressure, cholesterol, and blood sugar levels. Early detection of abnormalities helps in preventing complications.</li>
                                            <li><b>Blood Pressure Monitoring:</b> Keep track of your blood pressure levels to ensure they are within a healthy range. High blood pressure is a significant risk factor for heart disease.</li>
                                            <li><b>Cholesterol and Blood Sugar Levels:</b>Get regular screenings for cholesterol and blood sugar levels, as high levels can increase the risk of heart disease.</li>
                                            <li><b>Awareness and Education:</b>Stay informed about cardiovascular disease risks, symptoms, and prevention strategies. Educating yourself and others can lead to timely medical intervention and better health outcomes.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩Email sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}")
                else:
                    st.success('NEGATIVE')
                    with st.expander("Click here to see Test Report", expanded=True):
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.markdown(f"**Patient Name:** {name}")
                        with c2:
                            st.markdown(f"**Gender:** {gender}")
                        with c3:
                            st.markdown(f"**Age:** {Exact_Age}")

                        parameters = ["Height", "Weight", "Systolic Blood Pressure (mmHg)", "Diastolic Blood Pressure (mmHg)","Cholesterol", "Glucose", "Smoking", "Alcohol Intake"]
                        normal_ranges = ["Greater Then 160 cm", "55-79 kg", "90-120 mmHg", "60-90 mmHg","Normal - Above Normal", "Normal", "No", "No"]   
                        df = pd.DataFrame({"Parameter Name": parameters,"Patient Values":users_data,"Normal Range": normal_ranges})
                        st.table(df.reset_index(drop=True))
                        st.info("ℹ️ Do check your email for more details, Thank You.")   
                    
                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body ="""<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App</p>
                                        <h2 style="color:#09ab3b;">cardiovascular Disease Test Result: Negative</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Cardiovascular Disease Prevention:</h2>
                                        <ul>
                                            <li><b>Quit Smoking:</b> Smoking is a major risk factor for cardiovascular disease. Quitting smoking improves heart health and reduces the risk of heart attacks and strokes.</li>
                                            <li><b>Healthy Diet:</b> Consume a heart-healthy diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit salt, sugar, and saturated fat intake to maintain healthy cholesterol and blood pressure levels.</li>
                                            <li><b>Regular Exercise:</b> Engage in regular physical activity, such as walking, jogging, cycling, or swimming, for at least 30 minutes a day, most days of the week, to strengthen the heart and improve circulation.</li>
                                            <li><b>Maintain Healthy Weight:</b> Achieve and maintain a healthy weight to reduce the strain on the heart and lower the risk of hypertension and type 2 diabetes.</li>
                                            <li><b>Manage Stress:</b> Practice stress management techniques such as deep breathing, meditation, or yoga to reduce stress and its impact on heart health.</li>
                                            <li><b>Limit Alcohol Consumption:</b> Drink alcohol in moderation, if at all, as excessive alcohol intake can lead to high blood pressure, heart failure, and other cardiovascular problems.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Symptoms:</b> Be aware of cardiovascular symptoms such as chest pain, shortness of breath, irregular heartbeat, dizziness, and unexplained fatigue. Seek medical attention if you experience these symptoms.</li>
                                            <li><b>Regular Health Check-ups:</b> Schedule regular check-ups to monitor blood pressure, cholesterol, and blood sugar levels. Early detection of abnormalities helps in preventing complications.</li>
                                            <li><b>Blood Pressure Monitoring:</b> Keep track of your blood pressure levels to ensure they are within a healthy range. High blood pressure is a significant risk factor for heart disease.</li>
                                            <li><b>Cholesterol and Blood Sugar Levels:</b>Get regular screenings for cholesterol and blood sugar levels, as high levels can increase the risk of heart disease.</li>
                                            <li><b>Awareness and Education:</b>Stay informed about cardiovascular disease risks, symptoms, and prevention strategies. Educating yourself and others can lead to timely medical intervention and better health outcomes.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩Email sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}")
    with tab12:
         st.markdown("""
#### **What is Cardiovascular Disease?**
Cardiovascular disease (CVD) refers to a range of heart and blood vessel conditions, including coronary artery disease, heart attacks, heart failure, and strokes. CVD is one of the leading causes of death globally. The condition can be caused by blocked or narrowed blood vessels that reduce blood flow to the heart and other parts of the body.

#### **Types of Cardiovascular Disease:**
1. **Coronary Artery Disease (CAD)**: The buildup of plaque in the coronary arteries that supply blood to the heart muscle, leading to heart attacks.
2. **Heart Attack (Myocardial Infarction)**: Occurs when the blood supply to the heart is blocked, causing damage to the heart muscle.
3. **Heart Failure**: A condition where the heart cannot pump blood effectively to meet the body's needs.
4. **Stroke**: Occurs when blood flow to the brain is interrupted, resulting in brain damage.
5. **Peripheral Artery Disease (PAD)**: A condition where narrowed arteries reduce blood flow to the limbs.

#### **What Causes Cardiovascular Disease?**
CVD is caused by several factors, many of which are preventable. The main causes of cardiovascular disease include:
- **Unhealthy Diet:** A poor diet high in processed foods, fats, and salt can increase the risk.
- **Physical Inactivity:** A sedentary lifestyle can contribute to many cardiovascular risk factors, such as obesity and high blood pressure.
- **Smoking:** Smoking is one of the leading causes of heart disease and stroke.
- **Excessive Alcohol Consumption:** Drinking too much alcohol can increase blood pressure and contribute to heart disease.
- **High Blood Pressure:** High blood pressure (hypertension) forces the heart to work harder and can lead to heart damage over time.
- **High Cholesterol:** High levels of LDL (bad cholesterol) and low levels of HDL (good cholesterol) increase the risk of plaque buildup in the arteries.
- **Obesity:** Excess weight puts extra strain on the heart and increases the risk of developing heart disease.

#### **Symptoms of Cardiovascular Disease:**
The symptoms of cardiovascular disease can vary depending on the specific condition. Common symptoms include:
- **Chest Pain or Discomfort**
- **Shortness of Breath**
- **Fatigue**
- **Dizziness or Lightheadedness**
- **Swelling in the Legs, Ankles, or Feet**
- **Palpitations**
- **Nausea or Sweating**

#### **How to Prevent Cardiovascular Disease?**
While some risk factors like age and genetics cannot be controlled, there are many lifestyle changes that can reduce the risk of cardiovascular disease:
1. **Eat a Heart-Healthy Diet**
2. **Exercise Regularly**
3. **Quit Smoking**
4. **Manage Your Blood Pressure**
5. **Limit Alcohol Intake**
6. **Maintain a Healthy Weight**
7. **Control Your Cholesterol and Blood Sugar Levels**
""")
         st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px;'>
        &copy; 2025 | Developed by Rexson Epiron
    </div>
    """,
    unsafe_allow_html=True
)
##----------------------------------------------------------------------

if selected=='Diabetes Prediction':
    tab21, tab22 = st.tabs(["🩸 Diabetes Prediction", "🗒️ About Diabetes"])
    with tab21:
        model2 = pkl.load(open('Blood.pkl','rb'))
        df = pd.read_csv('diabetes.csv')
        st.title('Diabetes Prediction')
        name = st.text_input("Name")
        email = st.text_input("Email")
        email_sender = 'noreplymedipredict@gmail.com'##rexsonepiron@gmail.com
        password = 'bcys ibmv qvla tbig' 
        ##email_sender = 'rexsonepiron@gmail.com'
        ##password = 'pelc rkbn lfbf edgh' 
        st.warning('Please enter both Name and Email to proceed!') 

        if email:
            a1,a2,a3 = st.columns(3)
            
            with a1:
                Gender = st.selectbox('Select Your Gender',('Male','Female'))
                Pregnancies = st.number_input('Number of Pregnancies',0,20)
                Glucose = st.number_input('Glucose Level',0,200)
                
            with a2:
                BloodPressure = st.number_input('Blood Pressure Value',0,125)
                SkinThickness = st.number_input('Skin Thickness Value',0,99)
                Insulin = st.number_input('Insulin Level',0,846)
                
            with a3:
                BMI = st.number_input('BMI value',0,68)
                DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value',0,3)
                Age = st.number_input('Enter Your Age',18,81)
                

            if a3.button('Diabetes Test Result'):
                input_data_module=pd.DataFrame(
                    [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]],
                    columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
        'BMI', 'DiabetesPedigreeFunction', 'Age']
                    ) 
        

                Diabetes_Prediction = model2.predict(input_data_module)
                
                row_wise_df = pd.DataFrame(input_data_module)#.transpose()
                user_data = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction]
                patient_values = pd.DataFrame([user_data])
                if Diabetes_Prediction == 1:
                    st.error('POSITIVE')
                    with st.expander("Click here to see Test Report", expanded=True):
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.markdown(f"**Patient Name:** {name}")
                        with c2:
                            st.markdown(f"**Gender:** {Gender}")
                        with c3:
                            st.markdown(f"**Age:** {Age}")

                        parameters = ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness","Insulin", "BMI", "Diabetes Pedigree Function"]
                        normal_ranges = ["0-10", "70-125", "120/80", "8-25", "25-250", "18.5-24.9", "< 1"]   
                        units = [ "Number", "mg/dL", "mmHg", "mm", "mIU/L", "kg/m^2", "No units"]
                        df = pd.DataFrame({"Parameter Name": parameters,"Patient Values":user_data,"Normal Range": normal_ranges,"Unit": units })
                        st.table(df.reset_index(drop=True))
                        st.info("ℹ️ Do check your email for more details, Thank You.") 
                    
                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body = """<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App</p>
                                        <h2 style="color:#ff2b2b;">Lung Cancer Test Result: Positive</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Preventing Diabetes:</h2>
                                        <ul>
                                            <li><b>Maintain a Healthy Weight:</b> Being overweight increases the risk of type 2 diabetes. Aim for a balanced weight through a healthy diet and regular exercise.</li>
                                            <li><b>Eat a Balanced Diet:</b> Focus on foods high in fiber and low in sugar. Choose whole grains, fruits, vegetables, lean proteins, and healthy fats. Avoid sugary beverages and processed foods.</li>
                                            <li><b>Monitor Blood Sugar Levels:</b> If you are at risk, keep track of your blood glucose levels regularly and follow your healthcare provider’s recommendations.</li>
                                            <li><b>Stay Active:</b> Engage in at least 30 minutes of moderate physical activity most days of the week. Walking, cycling, swimming, and dancing are great options.</li>
                                            <li><b>Avoid Smoking:</b> Smoking increases the risk of type 2 diabetes and other serious health issues. Quitting smoking can improve your overall health.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Risk Factors:</b> Be aware of factors like family history, being overweight, sedentary lifestyle, high blood pressure, or being over 45 years of age.</li>
                                            <li><b>Recognize Early Symptoms:</b> Watch for early signs such as frequent urination, excessive thirst, unexplained weight loss, fatigue, blurred vision, or slow-healing wounds.</li>
                                            <li><b>Get Routine Screenings:</b> Regular blood sugar tests such as Fasting Blood Sugar (FBS), HbA1c, or Oral Glucose Tolerance Test (OGTT) can help detect diabetes or prediabetes in its early stages.</li>
                                            <li><b> Early Detection = Better Outcomes:</b> Detecting diabetes early helps in managing it more effectively, reducing the risk of complications such as heart disease, kidney damage, and nerve issues.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩Email sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}")
            
                else:
                    st.success('NEGATIVE')
                    with st.expander("Click here to see Test Report", expanded=True):
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.markdown(f"**Patient Name:** {name}")
                        with c2:
                            st.markdown(f"**Gender:** {Gender}")
                        with c3:
                            st.markdown(f"**Age:** {Age}")

                        parameters = ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness","Insulin", "BMI", "Diabetes Pedigree Function"]
                        normal_ranges = ["0-10", "70-125", "120/80", "8-25", "25-250", "18.5-24.9", "< 1"]   
                        units = [ "Number", "mg/dL", "mmHg", "mm", "mIU/L", "kg/m^2", "No units"]
                        df = pd.DataFrame({"Parameter Name": parameters,"Patient Values":user_data,"Normal Range": normal_ranges,"Unit": units })
                        st.table(df.reset_index(drop=True))
                        st.info("ℹ️ Do check your email for more details, Thank You.") 

                    try:
                        subject = "Thank You for using MediPredict Web App"
                        body ="""<html>
                                    <body>
                                        <p>Hello,</p>
                                        <p>Hope you're doing well today</p>
                                        <p>Thank you for using our Multiple Disease Prediction Web App</p>
                                        <h2 style="color:#09ab3b;">Lung Cancer Test Result: Negative</h2>
                                        <br>
                                        <h2 style="color:#004d99;">Tips for Preventing Diabetes:</h2>
                                        <ul>
                                            <li><b>Maintain a Healthy Weight:</b> Being overweight increases the risk of type 2 diabetes. Aim for a balanced weight through a healthy diet and regular exercise.</li>
                                            <li><b>Eat a Balanced Diet:</b> Focus on foods high in fiber and low in sugar. Choose whole grains, fruits, vegetables, lean proteins, and healthy fats. Avoid sugary beverages and processed foods.</li>
                                            <li><b>Monitor Blood Sugar Levels:</b> If you are at risk, keep track of your blood glucose levels regularly and follow your healthcare provider’s recommendations.</li>
                                            <li><b>Stay Active:</b> Engage in at least 30 minutes of moderate physical activity most days of the week. Walking, cycling, swimming, and dancing are great options.</li>
                                            <li><b>Avoid Smoking:</b> Smoking increases the risk of type 2 diabetes and other serious health issues. Quitting smoking can improve your overall health.</li>
                                        </ul>
                                        <h2 style="color:#004d99;">Early Detection and Screening:</h2>
                                        <ul>
                                            <li><b>Know the Risk Factors:</b> Be aware of factors like family history, being overweight, sedentary lifestyle, high blood pressure, or being over 45 years of age.</li>
                                            <li><b>Recognize Early Symptoms:</b> Watch for early signs such as frequent urination, excessive thirst, unexplained weight loss, fatigue, blurred vision, or slow-healing wounds.</li>
                                            <li><b>Get Routine Screenings:</b> Regular blood sugar tests such as Fasting Blood Sugar (FBS), HbA1c, or Oral Glucose Tolerance Test (OGTT) can help detect diabetes or prediabetes in its early stages.</li>
                                            <li><b> Early Detection = Better Outcomes:</b> Detecting diabetes early helps in managing it more effectively, reducing the risk of complications such as heart disease, kidney damage, and nerve issues.</li>
                                        </ul>
                                        <p><b>Note:</b> Individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.</p>
                                        <br>
                                        <p>Connect with us for more information.</p>
                                        <p>Thank you,</p>
                                        <p>Rexson Epiron A</p>
                                        <P>Data Science Aspirant</p>
                                    </body>
                                </html>"""
                        msg = MIMEMultipart()
                        msg['From'] = email_sender
                        msg['To'] = email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email_sender, password)
                        server.sendmail(email_sender, email, msg.as_string())
                        server.quit()
                        st.success('📩Email sent successfully! 🚀')
                    except Exception as e:
                                st.error(f"Failed to send email: {e}") 
    with tab22:
 

        st.markdown("## 🍬 All You Need to Know About Diabetes!")

        st.markdown("""
        Diabetes is a chronic health condition that affects how your body turns food into energy. It occurs when your blood glucose (blood sugar) is too high. Over time, having too much glucose in your blood can lead to serious health problems. But with proper care and lifestyle changes, diabetes can be managed effectively.
        """)

        st.markdown("### 🔍 What are the symptoms of diabetes?")
        st.markdown("""
        - Increased thirst and frequent urination  
        - Extreme hunger  
        - Unexplained weight loss  
        - Fatigue and irritability  
        - Blurred vision  
        - Slow-healing sores  
        - Frequent infections, such as gums or skin  
        - Numbness or tingling in hands or feet (especially in Type 2 diabetes)  
        """)

        st.markdown("### ⚠️ What are the risk factors for diabetes?")
        st.markdown("""
        - Being overweight or obese  
        - Sedentary lifestyle  
        - Family history of diabetes  
        - High blood pressure or cholesterol  
        - Age 45 or older  
        - History of gestational diabetes  
        - Polycystic ovary syndrome (PCOS)  
        - Unhealthy eating habits  
        """)

        st.info("👉 **Tip:** Early screening and adopting a healthy lifestyle with regular physical activity and a balanced diet can help prevent or delay Type 2 diabetes.")
        st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px;'>
        &copy; 2025 | Developed by Rexson Epiron
    </div>
    """,
    unsafe_allow_html=True
)
#----
if selected=='About us':
# About Us Section
   st.markdown("## 🔍 About Us")
   st.markdown(
    """
    <div style='font-size:16px; text-align: justify; padding: 15px; background-color: #f0f2f6; border-radius: 12px; line-height: 1.8;'>

    We are a team of passionate data scientists, developers, and healthcare researchers dedicated to improving lives through technology. Our **Multiple Disease Prediction System** is built with cutting-edge <b>Artificial Intelligence (AI)</b> models that assist in detecting critical illnesses at an early stage.<br><br>

    💡 <b>Why Early Diagnosis Matters?</b><br>
    Early detection of diseases such as Heart Disease, Diabetes, and Parkinson’s can significantly improve treatment outcomes and quality of life. Our platform provides an accessible, user-friendly interface where users can enter simple health parameters and receive instant predictions based on medically backed data.<br><br>

    🧠 <b>How AI Creates Awareness</b><br>
    By making health predictions easily available, we help users become more aware of their health status and encourage them to consult medical professionals before symptoms become severe. Our system doesn't replace a doctor — instead, it acts as a digital assistant to <b>raise awareness</b>, promote <b>preventive care</b>, and highlight the power of technology in saving lives.<br><br>

    🙌 <b>Our Mission</b><br>
    We believe in a future where AI and healthcare go hand-in-hand to support early diagnosis, drive personalized treatments, and reduce the burden on healthcare systems. This app is our humble step toward that vision.

    </div>
    """,
    unsafe_allow_html=True
)

   st.markdown("---")

# Feedback Section
   st.subheader("💬 We Value Your Feedback")

   with st.form("feedback_form", clear_on_submit=True):
      rating = st.slider("Rate your experience with our app", 1, 5, 3)
      message = st.text_area("Your Feedback")

      submit = st.form_submit_button("Submit Feedback")

      if submit:
        st.success("Thank you for your feedback! 😊")
        # You can save feedback to a database or send via email from here
        st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px;'>
        &copy; 2025 | Developed by Rexson Epiron
    </div>
    """,
    unsafe_allow_html=True
)
# elif not email:
#     st.error('please enter valid email address')

 #st.text_input('From', 'rexsonepiron@gmail.com', disabled=True)
# email_receiver = email


# File uploaders


# Hide the password input


# if st.button("Send Email"):

# Footer with profile details
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            text-align: left;
            font-size: 14px;
            border-top: 1px solid #ddd;
        }
        .footer img {
            border-radius: 50%;
            width: 25px;
            height: 25px;
            vertical-align: middle;
        }
        .footer a {
            text-decoration: none;
            color: black;
            font-weight: bold;
        }
        .footer span {
            margin-left: 5px;
        }
    </style>
    
    <div class="footer">
        Created by <a href="https://github.com/REXSONEPIRON" target="_blank">Rexson Epiron</a>
        <img src="https://avatars.githubusercontent.com/Rexson Epiron" alt="Profile Image">
        <span> | Hosted with Streamlit</span>
    </div>
    """,
    unsafe_allow_html=True
)



# if __name__=='__main__':
#     main()
