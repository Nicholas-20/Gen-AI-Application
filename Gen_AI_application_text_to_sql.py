import os
import streamlit as st
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(questions,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],questions])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
       print(row)
    return rows

prompt=[ 
    '''
     You are an expert in converting english language to SQL query!
     The sql database has the name STUDENT and the following column - NAME,CLASS
     SECTION and MARKS \n\n For example \n Example 1- how many entries of record is present?,
     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
     \n example 2 - tell me all the student studying in Data Science class?,
     the SQL command will be something like this SELECT * FROM STUDENT
     where CLASS="DATA SCIENCE";
     also the sql code should not have ``` in beginning or end and sql word in the output
     '''
]

st.set_page_config(page_title="I can Retrive any sql query")
st.header("Gemini App to Retrieve sql Data")
questions=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(questions,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("the response is: ")
    for row in data:
        print(row)
        st.header(row)
