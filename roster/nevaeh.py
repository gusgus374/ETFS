import streamlit as st

st.title("cold")

if st.button("snow"):
    st.write(":cold_face:")
    st.snow()

if st.button("Summer"):
    st.write(":surfer:")
    st.write(":sun_with_face:")

with st.expander("Show Nevaeh's code"):
    st.code(
        body='''
import streamlit as st

st.title("cold")

if st.button("snow"):
    st.write(":cold_face:")
    st.snow()

if st.button("Summer"):
    st.write(":surfer:")
    st.write(":sun_with_face:")
        ''',
        language="python",
        line_numbers=True
    )