import streamlit as st

st.title("Balloon day and Snow")
if st.button("Pop"):
    st.balloons()

if st.button("snow day"):
  st.snow()

with st.expander("Michya's Goal"):
   st.video("./resources/michya_goal_cece_skips.mp4")

with st.expander("Show Michya's code"):
    st.code(
        '''
import streamlit as st

st.title("Balloon day and Snow")
if st.button("Pop"):
    st.balloons()

if st.button("snow day"):
  st.snow()
''', language='python',line_numbers=True
    )