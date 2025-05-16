from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
def get_ollama_response(question):
    llm=Ollama(model="llama3",temperature=0.5)
    response=llm(question)
    return response
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input=st.text_input("input: ",key="input")

submit=st.button("Ask the Question")
if submit:
    response=get_ollama_response(input)
    st.subheader("The Response is")
    st.write(response)  