import streamlit as st
import openai

# Initialize the OpenAI API
openai.api_key = "YOUR_API_KEY"

# Create a form to collect user input
st.title("Resume Content Creator")
st.subheader("Please enter your information:")

with st.form("resume_form"):
    name = st.text_input("Name:")
    email = st.email_input("Email:")
    phone_number = st.text_input("Phone Number:")
    summary = st.text_input("Summary:")
    skills = st.text_input("Skills:")
    experience = st.text_input("Experience:")
    education = st.text_input("Education:")
    llm_temp = st.number_input('Temperature (0.0-1.0) Input how creative the API can be',value=.99)

    submit_button = st.form_submit_button("Create Resume")

# Define a function to send user input to OpenAI API
def create_resume(name, email, phone_number, summary, skills, experience, education):
    prompt = [{"role": "user", "content" : f"""
    Please create a professional and well-structured resume for {name}, highlighting their key skills, 
    experiences, and accomplishments. Use a clear and concise writing style, 
    ensuring the resume is tailored to their desired career path and targeted towards their chosen industry. 
    Incorporate relevant keywords and phrases throughout the resume to enhance its visibility during applicant tracking systems (ATS)."""},

    {"role": "user", "content" : "Personal Information"},

    {"role": "user", "content" : f"Name: {name}"},
    {"role": "user", "content" : f"Email: {email}"},
    {"role": "user", "content" : f"Phone Number: {phone_number}"},

    {"role": "user", "content" : f"Summary: {summary}"},

    

    {"role": "user", "content" : f"Skills: {skills}"},

    

    {"role": "user", "content" : f"Experience:{experience}"},


    {"role": "user", "content" : f"Education:{education}"},

    
    ]

    response = openai.ChatCompletion.create(
    #model="gpt-3.5-turbo-16k", 
    model = "gpt-3.5-turbo",
    temperature=llm_temp,
    messages=prompt)

    resume_text = response['choices'][0]['message']['content']
    return resume_text

# Create the resume with OpenAI API
if submit_button:
    resume_text = create_resume(name, email, phone_number, summary, skills, experience, education)
    st.success("Your resume is ready!")
    st.text(resume_text)
