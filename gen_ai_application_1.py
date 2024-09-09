# -*- coding: utf-8 -*-
"""Gen AI application 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jyzk_MmaYsvWz3_kHnPjVeTsbrLGBSjZ
"""

!python --version

!pip install streamlit

!pip install google-generativeai

!pip install python-dotenv

!pip install pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# GOOGLE_API_KEY="AIzaSyC3RNzsD4JDoLYgadrfG1pQT19sIbo9gvk"
# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai
# genai.configure(api_key=GOOGLE_API_KEY)
# model=genai.GenerativeModel("gemini-pro")
# def get_gemini_response(question):
#   response=model.generate_content(question)
#   return response.text
# #Initializing the streamlit app
# st.set_page_config(page_title="Q&A DEMO")
# st.header("GEMINI APPLICATION")
# input=st.text_input("Enter your question",key="input")
# submit=st.button("Submit")
# if submit:
#   response=get_gemini_response(input)
#   st.write(response)

!streamlit run app.py & npx localtunnel --port 8501

# Commented out IPython magic to ensure Python compatibility.
# %%writefile vision.py
# GOOGLE_API_KEY="AIzaSyC3RNzsD4JDoLYgadrfG1pQT19sIbo9gvk"
# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai
# from PIL import Image
# genai.configure(api_key=GOOGLE_API_KEY)
# model=genai.GenerativeModel("gemini-1.5-flash")
# def get_gemini_response(input,image):
#   if input!="":
#     response=model.generate_content([input,image])
#   else:
#     response=model.generate_content(image)
#   return response.text
# st.set_page_config(page_title="Gemini Image DEMO")
# st.header("GEMINI APPLICATION")
# input=st.text_input("Input prompt",key="input")
# uploaded_image=st.file_uploader("choose an image...",type=["jpeg","jpg","png"])
# image=""
# if uploaded_image is not None:
#   image= Image.open(uploaded_image)
#   st.image(image,caption="Uploaded Image",use_column_width=True)
# submit=st.button("Submit")
# if submit:
#   response=get_gemini_response(input,image)
#   st.write(response)
#

!streamlit run vision.py & npx localtunnel --port 8501

