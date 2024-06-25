import streamlit as st
import altair as alt

st.title("")

file = st.file_uploader("Pick an MP3 file")

st.audio(file)
st.title("Leo,azyrion,jamerson,Ayden")