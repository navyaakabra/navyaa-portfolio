import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Navyaa Kabra | Portfolio", layout="wide")

# --- Header ---
st.title("👩‍💻 Navyaa Kabra")
st.subheader("Data Analyst | ML Enthusiast | Python & Visualization")

st.markdown("""
📍 Jaipur, India  
📫 [kabranavyaa@gmail.com](mailto:kabranavyaa@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/navyaakabra/) | [GitHub](https://github.com/navyaakabra) | [Kaggle](https://www.kaggle.com/navyaakabra)  
""")

st.markdown("---")

# --- About Section ---
st.header("🧠 About Me")
st.write("""
I'm a Computer Science student at Manipal University Jaipur with a strong interest in data analysis and machine learning.
I love building practical, explainable models — and presenting them through intuitive, user-friendly interfaces.

My work spans predictive modeling, recommendation systems, and healthcare data analysis using tools like Python, Scikit-learn, SHAP, and Gradio.
""")

# --- Projects Section ---
st.header("📊 Projects")

st.subheader("🎬 Movie Quality Prediction & Recommendation")
st.markdown("""
- Trained Gradient Boosting model on metadata like genres, budget, and votes (R² = 0.56, ROC-AUC = 0.89)
- Used SHAP for interpretability and deployed an interactive Gradio app for real-time predictions  
🔗 [Kaggle Notebook](https://www.kaggle.com/code/navyaakabra/movie-quality-prediction)
""")

st.subheader("🩺 Digital Impact on Medical Adherence")
st.markdown("""
- Achieved 92% accuracy using an ensemble of logistic regression, SVM, XGBoost, and deep learning (AUC = 0.92)  
- Identified key behavioral predictors with feature importance plots  
🔗 [Kaggle Notebook](https://www.kaggle.com/code/navyaakabra/analysis-of-digital-impact-on-medical-adherence)
""")

st.subheader("🗃️ Optical Shop DBMS")
st.markdown("""
- Designed and implemented a relational database system for managing bookings, billing, and feedback  
🔗 [GitHub Repo](https://github.com/navyaakabra/optical-shop-dbms)
""")

# --- Resume ---
st.markdown("---")
st.header("📄 Resume")
st.markdown("[Download Resume (PDF)](https://drive.google.com/file/d/1-PpxBIRrqm3tDzmliccug7wLqNcINlxv/view?usp=drive_link)")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
