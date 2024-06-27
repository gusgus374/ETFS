import streamlit as st
import altair as alt

st.title("Hi I'm Eli")
if st.button("Balloons"):
    st.balloons()
    st.snow()

with st.expander("Show Eli's code"):
    st.code(
        body='''
import streamlit as st
import altair as alt

st.title("Hi I'm Eli")
if st.button("Balloons"):
    st.balloons()
    st.snow()
        ''',
        language="python",
        line_numbers=True
    )