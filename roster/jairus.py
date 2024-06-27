import streamlit as st

st.title("HI?")
if st.button("HI"):
    st.snow()
    #st.b()

with st.expander("Show Jairus's code"):
    st.code(
        body='''
import streamlit as st

st.title("HI?")
if st.button("HI"):
    st.snow()
    #st.b()
        ''',
        language="python",
        line_numbers=True
    )