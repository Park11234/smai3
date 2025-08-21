import os
import time
import streamlit as st
from PIL import Image
from MyLLM import geminiTxt
from MyLLM import geminiModel

#Sidebar
st.sidebar.markdown("clicked Page 3")

#Page
st.title("Page 3")

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
selected_option = st.radio("프로그래밍 언어를 선택하세요", ["JAVA","C","PYTHON"])
if st.button("SEND"):
    if text and selected_option:
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------

        result = geminiTxt(f"{text}\n{selected_option}를 이용하여 프로그래밍하라")
        my_bar.empty()
        st.info("답변입니다.")
        st.code(result, language=selected_option.lower())

    else:
        st.info("질문을 입력 하세요")
