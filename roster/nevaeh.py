import streamlit as st

st.title("cold")

if st.button("snow"):
    st.write(":cold_face:")
    st.snow()

with st.expander("Show Nevaeh's code"):
    st.code(
        body='''
import streamlit as st

st.title("cold")

if st.button("snow"):
    st.write(":cold_face:")
    st.snow()
        ''',
        language="python",
        line_numbers=True
    )