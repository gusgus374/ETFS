import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Samantha, and I love sleep")

st.header("I sleep on my side")

if st.button("See an example"):
    st.write("test")
    components.iframe("https://content.gallup.com/origin/gallupinc/GallupSpaces/Production/Cms/POLL/vdu8ggo1k0qxeo2vn9zoka.jpg", width = 900, height=400)

with st.expander("Show Samantha's code"):
    st.code(
        body='''
import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Samantha, and I love sleep")

st.header("I sleep on my side")

if st.button("See an example"):
    st.write("test")
    components.iframe("https://content.gallup.com/origin/gallupinc/GallupSpaces/Production/Cms/POLL/vdu8ggo1k0qxeo2vn9zoka.jpg", width = 900, height=400)
        ''',
        language="python",
        line_numbers=True
    )