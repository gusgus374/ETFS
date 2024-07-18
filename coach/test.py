import streamlit as st
st.set_page_config(
    page_title="test push",
    page_icon="./resources/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.sidebar.page_link("FootyLab.py", label=":seedling: Home Page ")
st.sidebar.page_link("pages/1_BootRoom.py", label=":star: Boot Room ")
st.sidebar.page_link("pages/codeBox.py", label=":computer: CODE BOX ")
st.sidebar.page_link("pages/coachGus.py", label=":pushpin: Coach's Examples ")
st.sidebar.page_link("pages/Class_Page.py", label=":bar_chart: Class Page")
st.sidebar.page_link("pages/2_US_Pro_Soccer.py", label=":earth_americas: :soccer: Investigator",disabled=False)
st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")

st.title("Hi")