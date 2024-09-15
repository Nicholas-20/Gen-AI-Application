import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel('gemini-1.5-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        return FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Health app")
st.header("Gemini Health app")
uploaded_file=st.file_uploader("Choose an image....",type=["jpeg","jpg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)

submit=st.button("Tell me about the total calories")

input_prompt="""
you are an expert in nutritionist where u need to see the food items from the image and calculate 
the toal claories, also provide the details of every food items with calorie intake in below format
1. item 1-no of calories
2. item 2-no of calories
----
----
Finally u can also mention whether the food is healthy or not, and also mention the percentage split
of the ratio of carbohydrates, fats, sugar and other important things required in our diet
"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The response is:")
    st.write(response)
