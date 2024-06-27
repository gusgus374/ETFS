import streamlit as st

st.title("lets play a game..")

if st.button("click 2 start.."):
    st.header("u have a set time")
    st.balloons()
    st.time_input("timer")

st.slider("pick a number", 0, 30)

with st.expander("Show Samantha's code"):
    st.code(
        body='''
import streamlit as st

st.title("lets play a game..")

if st.button("click 2 start.."):
    st.header("u have a set time")
    st.balloons()
    st.time_input("timer")

st.slider("pick a number", 0, 30)
        ''',
        language="python",
        line_numbers=True
    )