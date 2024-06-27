import streamlit as st

st.title("TV")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header("Boo")
if st.button("Jaylen"):
    st.header("Haha")
if st.button("Mona"):
      st.header("Law and Order")

with st.expander("Show Jamiya's code"):
    st.code(
        body='''
import streamlit as st

st.title("TV")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header("Boo")
if st.button("Jaylen"):
    st.header("Haha")
if st.button("Mona"):
      st.header("Law and Order")
        ''',
        language="python",
        line_numbers=True
    )