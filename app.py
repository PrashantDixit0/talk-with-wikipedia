from chat_retreival import retrieverSetup, chat

import os
import streamlit as st
    
# OPENAI_KEY =os.environ["OPENAI_API_KEY"]

@st.cache_resource
def loading_wiki_pages(query):
    #setting up reteriver
    qa = retrieverSetup(query, OPENAI_KEY)
    return qa
        

st.header('Talk with Wikipedia Pages', divider='rainbow')

query_wiki = st.text_input('Enter Topic')
OPENAI_KEY = st.text_input('openai')
if query_wiki :
    # Chat Agent getting ready
    qa = loading_wiki_pages(query_wiki)
        

prompt = st.chat_input("Talk with Wikipedia Pages")

if prompt:
    st.write(f"{prompt}")
    #chat using retreiver
    answer = chat(qa, prompt)
    
    st.write(f"{answer}")