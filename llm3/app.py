import streamlit as st

page_main = st.Page("main.py", title="main Page", icon="🎈")
page_1 = st.Page("p1.py", title="Page1", icon="🎈")
page_2 = st.Page("p2.py", title="Page2", icon="🎈")
page_3 = st.Page("p3.py", title="Page3", icon="🎈")
page_4 = st.Page("p4.py", title="Page4", icon="🎈")
page_5 = st.Page("p5.py", title="Page5", icon="🎈")
page_6 = st.Page("p6.py", title="Page6", icon="🎈")
page_7 = st.Page("p7.py", title="Page7", icon="☎")
page_8 = st.Page("p8.py", title="Page8", icon="☎")
page_9 = st.Page("p9.py", title="Page9", icon="☎")
page_10 = st.Page("p10.py", title="Page10", icon="☎")
page_11 = st.Page("p11.py", title="Page11", icon="☎")
page_12 = st.Page("p12.py", title="Page12", icon="☎")
page_13 = st.Page("p13.py", title="Page13", icon="☎")



page = st.navigation([page_main,page_1,page_2,page_3,page_4,page_5,page_6,page_7,page_8,page_9,page_10,page_11,page_12,page_13])

page.run()