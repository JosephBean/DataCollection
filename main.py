import streamlit as st

st.set_page_config(
    page_title="1팀 프로젝트",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Data Collection")

# st.link_button(
#     label="페이지1 이동",
#     url="./pages/1_page1.py"
# )

st.page_link(
    page="./pages/1_page1.py",
    label="페이지1 이동",
    help="이동하면 알껄!!"
)