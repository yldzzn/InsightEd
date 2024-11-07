# Import necessary libraries
import streamlit as st

# Set up a bilingual toggle (English and Turkish)
language = st.sidebar.selectbox("Select Language / Dil Seçin", ["English", "Turkish"])

# Set the company name based on language selection
company_name = "InsightEd" if language == "English" else "EduVeri"

# Set up the title and a header
st.title(f"Welcome to {company_name}")
st.header("Empowering Education with Intelligent Insights")

# Define a function for the homepage
def homepage():
    if language == "English":
        st.subheader("Transforming Education Through Data")
        st.write("""
            InsightEd leverages AI and analytics to provide educators with actionable insights. 
            We help institutions optimize student success through real-time analytics, 
            predictive insights, and proactive interventions.
        """)
    else:
        st.subheader("Eğitimi Veri ile Dönüştürme")
        st.write("""
            EduVeri, eğitimi desteklemek için yapay zeka ve analitik kullanarak eğitimcilere eyleme geçirilebilir 
            içgörüler sunar. Kurumların öğrenci başarısını gerçek zamanlı analiz, öngörüler ve proaktif 
            müdahalelerle optimize etmesine yardımcı olur.
        """)

# Define a function for the solutions page
def solutions_page():
    if language == "English":
        st.subheader("Our Solutions")
        st.write("""
            - **Real-Time Analytics Dashboard**: Access real-time insights into student engagement and progress.
            - **Predictive Analytics**: Identify at-risk students early and suggest proactive measures.
            - **Personalized Learning Paths**: Support personalized education through data-driven recommendations.
            - **Impact Measurement**: Evaluate the effectiveness of educational interventions.
            - **Compliance and Privacy**: Ensuring data protection with GDPR-compliant practices.
        """)
    else:
        st.subheader("Çözümlerimiz")
        st.write("""
            - **Gerçek Zamanlı Analitik Gösterge Tablosu**: Öğrenci katılımı ve ilerlemesi hakkında gerçek zamanlı içgörüler.
            - **Tahmin Analitiği**: Risk altındaki öğrencileri erken tespit etme ve proaktif önlemler sunma.
            - **Kişiselleştirilmiş Öğrenme Yolları**: Veri odaklı önerilerle kişiselleştirilmiş eğitimi destekleme.
            - **Etkililik Ölçümü**: Eğitim müdahalelerinin etkisini değerlendirme.
            - **Gizlilik ve Uyumluluk**: GDPR uyumlu veri koruma uygulamaları.
        """)

# Define a function for the features page
def features_page():
    if language == "English":
        st.subheader("Key Features")
        st.write("""
            - **Interactive Dashboard**: A visually engaging, user-friendly platform for educators.
            - **Data-Driven Alerts**: Automated notifications to identify students needing additional support.
            - **Behavioral Analytics**: Track key behavioral indicators linked to academic performance.
            - **Automated Reports**: Generate reports for educators, students, and parents to promote transparency.
        """)
    else:
        st.subheader("Temel Özellikler")
        st.write("""
            - **Etkileşimli Gösterge Tablosu**: Eğitimciler için kullanıcı dostu, görsel olarak çekici bir platform.
            - **Veriye Dayalı Uyarılar**: Ek destek gerektiren öğrencileri tespit eden otomatik bildirimler.
            - **Davranış Analitiği**: Akademik performansla bağlantılı davranışsal göstergeleri izleme.
            - **Otomatik Raporlar**: Eğitimciler, öğrenciler ve veliler için şeffaflığı teşvik eden raporlar oluşturma.
        """)

# Define a function for the about us page
def about_page():
    if language == "English":
        st.subheader("About Us")
        st.write("""
            InsightEd was founded with the mission to harness the power of data to transform education. 
            Our team consists of data scientists, educators, and AI experts committed to supporting 
            educational institutions in their journey toward data-driven success.
        """)
    else:
        st.subheader("Hakkımızda")
        st.write("""
            EduVeri, eğitimi dönüştürmek için verinin gücünü kullanma misyonuyla kuruldu. 
            Ekibimiz, eğitim kurumlarını veri odaklı başarı yolunda desteklemeye kendini adamış 
            veri bilimciler, eğitimciler ve yapay zeka uzmanlarından oluşmaktadır.
        """)

# Define a function for the contact page
def contact_page():
    if language == "English":
        st.subheader("Contact Us")
        st.write("""
            We’d love to hear from you! Whether you have a question about features, pricing, or anything else, 
            our team is ready to answer all your questions.
        """)
        st.write("**Email**: contact@insighted.com")
        st.write("**Phone**: +44 123 456 789")
    else:
        st.subheader("Bize Ulaşın")
        st.write("""
            Sorularınızı duymaktan memnuniyet duyarız! Özellikler, fiyatlandırma veya başka konularda 
            herhangi bir sorunuz varsa, ekibimiz tüm sorularınızı yanıtlamaya hazır.
        """)
        st.write("**E-posta**: iletisim@eduveri.com")
        st.write("**Telefon**: +90 123 456 789")

# Sidebar menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Solutions", "Features", "About Us", "Contact"])

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

