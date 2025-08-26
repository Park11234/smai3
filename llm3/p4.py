import os
import time
import streamlit as st
from PIL import Image
from MyLLM import geminiTxt, progressBar
from MyLLM import geminiModel

#Sidebar
st.sidebar.markdown("clicked Page 4")

#Page
st.title("Page 4")

text = st.text_area(label="질문을 입력:",
                    placeholder="질문을 입력하세요")

language = st.selectbox("언어를 선택하세요", ["English", "Japanese", "Chinese"])

if st.button("SEND"):
    if text and language:
        st.info(f"선택하신 언어는:{language}")
        my_bar = progressBar("Operation in progress. Please wait.")
        result = geminiTxt(f"{language}로 {text}를 번역해줘")
        my_bar.empty()
        st.info(result)

    else:
        st.info("질문과 언어를 입력하세요")
