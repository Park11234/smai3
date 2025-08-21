import  streamlit as st

page_main = st.Page("main.py", title="main Page", icon="🎈")
page_1 = st.Page("p1.py", title="Page1", icon="🎈")
page_2 = st.Page("p2.py", title="Page2", icon="🎈")
page_3 = st.Page("p3.py", title="Page3", icon="🎈")
page_4 = st.Page("p4.py", title="Page4", icon="🎈")
page_5 = st.Page("p5.py", title="Page5", icon="🎈")




page = st.navigation([page_main,page_1,page_2,page_3,page_4,page_5])

page.run()