import streamlit as st

st.title("Mona stills needs to give me 20 $")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header(":star:")
if st.button("Jaylen"):
    st.header(":cow:")
if st.button("Mona"):
      st.header(":scales:")
if st.button("Love"):
    st.header("Not Mona")
if st.button("Stop"):
    st.header("Talking to my mom")
if st.button("zoo"):
    st.header(":monkey:")
if st.button("Elsa"):
    st.write(":cold_face:")
    st.snow()
if st.button("Happy birthday"):
    st.balloons()
if st.button("Taurus"):
     st.header("Jamiya")
with st.expander("Show Jamiya's code"):
    st.code(
        body='''
import streamlit as st

st.title("Mona stills needs to give me 20 $")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header(":star:")
if st.button("Jaylen"):
    st.header(":cow:")
if st.button("Mona"):
      st.header(":scales:")
if st.button("Love"):
    st.header("Not Mona")
if st.button("Stop"):
    st.header("Talking to my mom")
if st.button("zoo"):
    st.header(":monkey:")
if st.button("Elsa"):
    st.write(":cold_face:")
    st.snow()
if st.button("Happy birthday"):
    st.balloons()
if st.button("Taurus"):
     st.header("Jamiya")
        ''',
        language="python",
        line_numbers=True
    )