import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from google.cloud import vision

# Load environment variables
load_dotenv()

# Define API configuration (example; adjust based on the actual API)
# Ensure you replace the API key with the correct one for the service you are using
# If using Google Cloud Vision API, you might not need this key configuration here
api_key = os.getenv("AIzaSyCIFMm64cQ2mDvpe8IAVlE5yHQ2sMtmb74")  # Update with your actual key variable name if needed

def get_gemini_response(prompt):
    # Placeholder function for calling the API
    # Update this based on the actual API call
    # For demonstration, using a static response
    response = {"JD Match": "85%", "MissingKeywords": ["Python"], "Profile Summary": "Experienced Data Scientist"}
    return response

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Define the prompt template
input_prompt = """
Hey Act Like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
the best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.
Resume: {text}
Description: {jd}

I want the response as per below structure:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

# Streamlit app
with st.sidebar:
    st.title("Smart ATS for Resumes")
    st.subheader("About")
    st.write("This sophisticated ATS project, developed with Gemini Pro and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision of the candidate evaluation process for discerning talent acquisition professionals.")
    
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
    - [makersuite API Key](https://makersuite.google.com/)
    - [Github](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro) Repository
    """)
    
    add_vertical_space(5)
    st.write("Made with ❤ by Mallikarjun Teli.")

st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt = input_prompt.format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.subheader("Response")
        st.json(response)
    else:
        st.error("Please upload a PDF file.")
