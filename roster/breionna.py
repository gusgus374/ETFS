import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Bre, and I love dance")

st.header("My favorite style of dance is Majorette")

if st.button("See an example"):
    st.write("test")
    components.iframe("https://www.youtube.com/embed/xfViiapeJyo?si=bu0ZLdVlyuh2AYlH", width = 300)

with st.expander("Show Bre's code"):
    st.code(
        body='''
import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Bre, and I love dance")

st.header("My favorite style of dance is Majorette")

if st.button("See an example"):
    st.write("test")
    components.iframe("https://www.youtube.com/embed/xfViiapeJyo?si=bu0ZLdVlyuh2AYlH", width = 300)
        ''',
        language="python",
        line_numbers=True
    )