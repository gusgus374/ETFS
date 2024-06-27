import streamlit as st
if st.button("hi"):
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()

with st.expander("Show Garrett's code"):
    st.code(
        body='''
import streamlit as st
if st.button("hi"):
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
    st.snow()
        ''',
        language="python",
        line_numbers=True
    )