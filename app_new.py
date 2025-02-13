import streamlit as st
from transformers import pipeline
import random

# Load a pre-trained conversational model
chatbot_pipeline = pipeline("text-generation", model="gpt2")  # Replace "gpt2" with a fine-tuned healthcare-specific model if available

# Predefined prescriptions for common symptoms (example logic)
symptom_diagnosis_mapping = {
    "fever": {
        "condition": "Possible Viral Infection or Flu",
        "prescription": "Take paracetamol (500 mg) every 8 hours. Drink plenty of fluids. If symptoms persist beyond 3 days, consult a doctor."
    },
    "cough": {
        "condition": "Possible Respiratory Infection",
        "prescription": "Take a cough syrup like Benadryl (5ml) every 6 hours. Stay hydrated and avoid cold drinks."
    },
    "chest pain": {
        "condition": "Potential Heart Issue or Acid Reflux",
        "prescription": "Immediate consultation with a cardiologist is recommended. Avoid fatty meals."
    },
    "headache": {
        "condition": "Possible Migraine or Stress",
        "prescription": "Take ibuprofen (200 mg) if needed. Rest in a quiet, dark room."
    },
    "nausea": {
        "condition": "Gastric Upset or Motion Sickness",
        "prescription": "Take domperidone (10 mg) before meals. Avoid oily and spicy food."
    },
    "diarrhea": {
        "condition": "Gastroenteritis or Food Poisoning",
        "prescription": "Drink oral rehydration solutions (ORS) frequently. Take loperamide if needed. Maintain hygiene."
    },
    "skin rash": {
        "condition": "Possible Allergic Reaction or Dermatitis",
        "prescription": "Apply calamine lotion. For severe itching, consider an antihistamine like cetirizine."
    },
    "shortness of breath": {
        "condition": "Potential Asthma or COVID-19 Symptoms",
        "prescription": "Use an inhaler if prescribed. Seek immediate medical attention if symptoms persist."
    },
    "joint pain": {
        "condition": "Possible Arthritis or Physical Strain",
        "prescription": "Apply hot compress. Take ibuprofen (200 mg) if needed. Consult an orthopedist if pain persists."
    },
    "sore throat": {
        "condition": "Possible Throat Infection",
        "prescription": "Gargle with warm salt water. Take lozenges for relief. If severe, consult a doctor."
    },
    "fatigue": {
        "condition": "Possible Anemia or Vitamin Deficiency",
        "prescription": "Increase iron-rich foods like spinach. Take vitamin B12 supplements if prescribed."
    },
    "high blood pressure": {
        "condition": "Hypertension",
        "prescription": "Reduce salt intake. Take prescribed antihypertensive medications. Regular monitoring is essential."
    },
    "high blood sugar": {
        "condition": "Potential Diabetes or Hyperglycemia",
        "prescription": "Avoid sugary foods. Monitor glucose levels. Take prescribed diabetic medications."
    }
}

# Chatbot response logic
def healthcare_chatbot(user_input):
    # Check for predefined symptoms in user input
    for symptom, details in symptom_diagnosis_mapping.items():
        if symptom in user_input.lower():
            condition = details["condition"]
            prescription = details["prescription"]
            return f"It seems like you are concerned about {symptom}. \nCondition: {condition} \nPrescription: {prescription}"

    # Generate conversational response using the AI model
    response = chatbot_pipeline(user_input, max_length=500, num_return_sequences=1)
    return response[0]['generated_text']

# Streamlit web app interface
def main():
    st.title("AI-Powered Healthcare Assistant")
    st.write("Your virtual assistant for healthcare advice and information.")

    # Display user query input
    user_input = st.text_input("How can I assist you today?", "")

    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("**You:**", user_input)
            with st.spinner("Processing your query..."):
                response = healthcare_chatbot(user_input)
            st.write("**Healthcare Assistant:**", response)
        else:
            st.write("Please enter your query.")

if __name__ == "__main__":
    main()
