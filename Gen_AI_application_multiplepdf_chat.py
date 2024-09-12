from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import pickle

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def get_pdf_text(pdf_docs):
  text=""
  for pdf in pdf_docs:
    pdf_reader=PdfReader(pdf)
    for page in pdf_reader.pages:
      text+=page.extract_text()
  return text

def get_text_chunk(text):
  text_splitter=RecursiveCharacterTextSplitter(
      chunk_size=10000,
      chunk_overlap=1000)
  chunks=text_splitter.split_text(text)
  return chunks

def get_vector_chunks(text_chunks):
  embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
  vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
  vector_store.save_local("faiss-index")

def get_conversational_chain(vector_store):
  prompt_template="""
  Answer the question as detailed as possible from the given context, make sure
  to provide all the details , if the answer is not in the provided context just
  say "answer is not available in the context", dont provide the wrong answer\n\n
  Context:"\n{context}?\n
  Answer:"\n{question}\n

  Answer:
  """
  model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
  prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
  chain=load_qa_chain(model,chain_type="stuff")
  return chain

def user_input(user_question):
  embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
  new_db=FAISS.load_local("faiss-index",embeddings)
  docs=new_db.similarity_search(user_question)
  chain=get_conversational_chain()
  response=chain(
      {"input_document":docs,"question":user_question},
      return_only_outputs=True)
  print(response)
  st.write("Reply:", response["output_text"])

def main():
  st.set_page_config("chat pdf")
  st.header("Chat with pdf using Gemini")
  user_question=st.text_input("Ask a question from the pdf file")
  if user_question:
    user_input(user_question)
  with st.sidebar:
    st.title("Menu")
    pdf_docs=st.file_uploader("Upload your pdf files")
    if st.button("Submit & Process"):
      with st.spinner("Processing"):
        raw_text=get_pdf_text(pdf_docs)
        text_chunks=get_text_chunk(raw_text)
        get_vector_chunks(text_chunks)
        st.success("Done")

if __name__=="__main__":
  main()
