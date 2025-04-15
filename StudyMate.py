# app.py
import streamlit as st
from PyPDF2 import PdfReader
import openai
import datetime

openai_key = st.secrets["OPENAI_KEY"]
st.title("📘 StudyMate AI - Syllabus Parser")

uploaded_file = st.file_uploader("📤 Upload your syllabus (PDF)", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() or "" for page in reader.pages])
    st.success("✅ PDF Uploaded and Text Extracted")

    # Show preview of text
    if st.checkbox("🔍 Show extracted syllabus text"):
        st.text_area("Extracted Text", text[:2000])

    if st.button("🧠 Extract Deliverables"):
        with st.spinner("Asking GPT-4 Turbo..."):
            prompt = f"""
You are an academic assistant. Extract a list of tasks from this syllabus. 
Each task should include: task_name, deadline (YYYY-MM-DD), and priority (High/Medium/Low).

Syllabus:
{text}
            """
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response['choices'][0]['message']['content']
            st.success("✅ Deliverables Extracted")
            st.text_area("📋 Output", output, height=300)
