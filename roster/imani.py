import streamlit as st

if st.button("Press to play =) "):
    st.balloons()
    st.title("can u spot the diffrence")
    st.title(":laughing:")
    st.title("jk")

with st.expander("Show Imani's code"):
    st.code(
        body='''
import streamlit as st

if st.button("Press to play =) "):
    st.balloons()
    st.title("can u spot the diffrence")
    st.title(":laughing:")
    st.title("jk")
        ''',
        language="python",
        line_numbers=True
    )