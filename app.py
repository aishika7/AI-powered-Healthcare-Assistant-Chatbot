import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')


# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response logic (or use a model to generate responses)
def healthcare_chatbot(user_input):
    # Simple rule-based keywords to respond
    if "condition" in user_input:
        for symptom, details in symptom_diagnosis_mapping.items():
            if symptom in user_input.lower():
                condition = details["condition"]
                prescription = details["prescription"]
                return f"It seems like you are concerned about {symptom}. \nCondition: {condition} \nPrescription: {prescription}"
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        # For other inputs, use the Hugging Face model to generate a response
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        # Specifies the maximum length of the generated text response, including the input and the generated tokens.
        # If set to 3, the model generates three different possible responses based on the input.
        return response[0]['generated_text']
    
    
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


# Streamlit web app interface
def main():
    # Set up the web app title and input area
    st.title("Healthcare Assistant Chatbot")
    
    # Display a simple text input for user queries
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query. Please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
