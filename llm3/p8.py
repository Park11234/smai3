import streamlit as st
from MyLLM import save_uploadedfile, makeAudio, openAiModelArg, makeMsg, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")

system = st.text_input("SYSTEM", placeholder="system을 입력")
text = st.text_input("질문을 입력", placeholder="질문을 입력")

if st.button("SEND"):

    if system and text:
        st.info(text)
        makeAudio(text, "temp1.mp3")
        st.audio("audio/temp1.mp3", autoplay=True, width=1)
        msg = makeMsg(system, text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = openAiModelArg("gpt-4o", msg)
        my_bar.empty()
        st.info(result)
        makeAudio(result,"temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True, width=1)

    else:
        st.info("입력하세요")
        st.audio("audio/retry.mp3", autoplay=True, width=1)
