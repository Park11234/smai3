import base64
import os
import streamlit as st
from PIL import Image
from MyLLM import makeAudio, makeMsg, progressBar, openAiModelArg, save_uploadedfile, openAiModel, encode_image

# Sidebar
st.sidebar.markdown("clicked Page 9")

# Page
st.title("Page 9")



file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file, st )

    text = st.text_area(label="질문입력:",
                        placeholder="질문을 입력 하세요")

    if st.button("SEND"):
        makeAudio(text, "temp1.mp3")
        st.audio("audio/temp1.mp3", autoplay=True, width=1)
        base64img = encode_image("img/"+file.name)
        model = openAiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
                {"role": "user", "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url":
                        {"url": f"data:image/jpg;base64,{base64img}"}
                     }]}],
            temperature=0.0,)

        st.info(response.choices[0].message.content)
        makeAudio(response.choices[0].message.content, "result.mp3")
        st.audio("audio/result.mp3", autoplay=True, width=1)
        my_bar.empty()

    else:
        st.info("입력하세요")
        st.audio("audio/retry.mp3", autoplay=True, width=1)




