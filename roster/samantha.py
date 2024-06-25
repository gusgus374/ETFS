import streamlit as st

st.title("lets play a game..")

if st.button("click 2 start.."):
    st.header("u have a set time")
    st.balloons()
    st.time_input("timer")

st.slider("pick a number", 0, 30)