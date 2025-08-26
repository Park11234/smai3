import streamlit as st

page_main = st.Page("main.py", title="main Page", icon="♨")
page_1 = st.Page("p1.py", title="Page1", icon="🎈")
page_2 = st.Page("p2.py", title="Page2", icon="🎈")


page = st.navigation([page_main,page_1,page_2])

page.run()