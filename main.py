import streamlit as st
from PIL import Image

# Load any images or logos you have (add these images to the same folder or specify paths)
# Replace 'logo.png' and 'dashboard.png' with actual images
# logo = Image.open('logo.png')
# dashboard_img = Image.open('dashboard.png')

# Set custom styling and configurations for a clean, professional look
st.set_page_config(page_title="InsightEd | EduVeri", page_icon=":books:", layout="centered")

# Sidebar for language selection
language = st.sidebar.selectbox("Select Language / Dil Seçin", ["English", "Turkish"])

# Set company name and page styling based on language
company_name = "InsightEd" if language == "English" else "EduVeri"
st.sidebar.image('logo.png', use_column_width=True)  # Replace with actual logo image
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Solutions", "Features", "About Us", "Contact"])

# Apply custom CSS styling
st.markdown("""
    <style>
    .title-text { font-size: 32px; color: #2E4053; font-weight: bold; }
    .subheader-text { font-size: 24px; color: #1C2833; font-weight: bold; }
    .body-text { font-size: 16px; color: #515A5A; }
    .highlight { color: #2874A6; font-weight: bold; }
    .footer { font-size: 12px; color: #AAB7B8; }
    .stButton > button { font-size: 18px; color: #FFFFFF; background-color: #2874A6; }
    </style>
    """, unsafe_allow_html=True)

# Define a function for the homepage
def homepage():
    st.image('dashboard.png', use_column_width=True)  # Replace with a relevant image
    st.markdown(f"<div class='title-text'>Welcome to {company_name}</div>", unsafe_allow_html=True)
    if language == "English":
        st.markdown("<div class='subheader-text'>Transforming Education Through Data</div>", unsafe_allow_html=True)
        st.markdown("""
            <p class='body-text'>
            At <span class='highlight'>InsightEd</span>, we harness the power of AI and analytics to provide educators 
            with actionable insights. Our platform helps institutions optimize student success with real-time analytics, 
            predictive insights, and proactive interventions.
            </p>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='subheader-text'>Eğitimi Veri ile Dönüştürme</div>", unsafe_allow_html=True)
        st.markdown("""
            <p class='body-text'>
            <span class='highlight'>EduVeri</span>, yapay zeka ve analitiğin gücünden faydalanarak eğitimcilere 
            eyleme geçirilebilir içgörüler sunar. Platformumuz, kurumların öğrenci başarısını optimize etmesine 
            yardımcı olur ve gerçek zamanlı analiz, öngörüler ve proaktif müdahaleler sunar.
            </p>
        """, unsafe_allow_html=True)

# Define functions for other pages with similar styling enhancements
def solutions_page():
    st.markdown("<div class='title-text'>Our Solutions</div>", unsafe_allow_html=True)
    solutions = [
        ("Real-Time Analytics Dashboard", "Access real-time insights into student engagement and progress."),
        ("Predictive Analytics", "Identify at-risk students early and suggest proactive measures."),
        ("Personalized Learning Paths", "Support personalized education through data-driven recommendations."),
        ("Impact Measurement", "Evaluate the effectiveness of educational interventions."),
        ("Compliance and Privacy", "Ensuring data protection with GDPR-compliant practices.")
    ]
    for title, description in solutions:
        st.markdown(f"### {title}")
        st.write(description)

def features_page():
    st.markdown("<div class='title-text'>Key Features</div>", unsafe_allow_html=True)
    features = [
        ("Interactive Dashboard", "A visually engaging, user-friendly platform for educators."),
        ("Data-Driven Alerts", "Automated notifications to identify students needing additional support."),
        ("Behavioral Analytics", "Track key behavioral indicators linked to academic performance."),
        ("Automated Reports", "Generate reports for educators, students, and parents to promote transparency.")
    ]
    for title, description in features:
        st.markdown(f"### {title}")
        st.write(description)

def about_page():
    st.markdown("<div class='title-text'>About Us</div>", unsafe_allow_html=True)
    if language == "English":
        st.write("""
            InsightEd was founded with the mission to harness the power of data to transform education. 
            Our team consists of data scientists, educators, and AI experts committed to supporting 
            educational institutions in their journey toward data-driven success.
        """)
    else:
        st.write("""
            EduVeri, eğitimi dönüştürmek için verinin gücünü kullanma misyonuyla kuruldu. 
            Ekibimiz, eğitim kurumlarını veri odaklı başarı yolunda desteklemeye kendini adamış 
            veri bilimciler, eğitimciler ve yapay zeka uzmanlarından oluşmaktadır.
        """)

def contact_page():
    st.markdown("<div class='title-text'>Contact Us</div>", unsafe_allow_html=True)
    contact_info = {
        "English": {
            "description": "We’d love to hear from you! Whether you have a question about features, pricing, or anything else, our team is ready to answer all your questions.",
            "email": "contact@insighted.com",
            "phone": "+44 123 456 789"
        },
        "Turkish": {
            "description": "Sorularınızı duymaktan memnuniyet duyarız! Özellikler, fiyatlandırma veya başka konularda herhangi bir sorunuz varsa, ekibimiz tüm sorularınızı yanıtlamaya hazır.",
            "email": "iletisim@eduveri.com",
            "phone": "+90 123 456 789"
        }
    }
    selected_lang = "English" if language == "English" else "Turkish"
    st.write(contact_info[selected_lang]["description"])
    st.write(f"**Email**: {contact_info[selected_lang]['email']}")
    st.write(f"**Phone**: {contact_info[selected_lang]['phone']}")

# Render pages based on sidebar selection
if menu == "Home":
    homepage()
elif menu == "Solutions":
    solutions_page()
elif menu == "Features":
    features_page()
elif menu == "About Us":
    about_page()
elif menu == "Contact":
    contact_page()

# Footer section
st.markdown("<div class='footer'>© 2023 InsightEd / EduVeri. All rights reserved.</div>", unsafe_allow_html=True)
