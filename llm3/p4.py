import os
import time
import streamlit as st
from PIL import Image
from MyLLM import geminiTxt
from MyLLM import geminiModel

#Sidebar
st.sidebar.markdown("clicked Page 4")

#Page
st.title("Page 4")

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
selected_option = st.radio("언어를 선택하세요", ["일본어","영어","독일어"])
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

        result = geminiTxt(f"{text}\n{selected_option}를 이용하여 되묻지말고 모든 옵션을 임의로 결정하여 선택한 옵션으로 번역하라")
        my_bar.empty()

        st.info(result)

    else:
        st.info("질문을 입력 하세요")
