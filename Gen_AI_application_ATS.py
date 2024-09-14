import os
import streamlit as st
import pdf2image
from PIL import Image
import io
import base64
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploade_file):
    if uploade_file is not None:
        images=pdf2image.convert_from_bytes(uploade_file.read(),poppler_path=r'C:\Program Files (x86)\poppler\Library\bin')
        first_page=images[0]
        img_byte_arr=io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr=img_byte_arr.getvalue()
        pdf_parts=[
            {
                "mime_type":"image/jpeg",
                "data":base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking system")
input_text=st.text_area("Job description:",key="input")
uploaded_file=st.file_uploader("upload your file(PDF)")

if uploaded_file is not None:
    st.write("PDF UPLOADED SUCCESFULLY")

submit1=st.button('Tell me about the resume')
#submit2=st.button('how can i improvise my skill')
submit3=st.button('Percentage match')

input_prompt1='''
You are an experienced HR with tech exprience in the field of any one job role from Data Science,Full stack web development,Big data Engineering,
DEVOPS,Data Analyst your task is to review the provided resume against the job description of these profiles
please share your professional evaluation on whether the candidate's profile aligns with the role
Highlight the strenght and weaknesses of the applicant in relation to the specified role description
'''
input_prompt3='''
You are a skilled ATS(Applicaiton tracker system) scanner with a deep understanding of any one job role from
Data Science, Full stack web development, Big data Engineering, DEVOPS, Data Analyst and ATS functionality,
your task is to evaluate the resume against the provided job description. give me the percentage of match 
if the resume matches the job description. First the output should come as percentage and then keywords missing
and last final thoughts
'''

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("please upload the resume")

