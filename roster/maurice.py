import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Maurice")

components.iframe(src="https://www.youtube.com/embed/j1nothJ1_O0?si=8HZwTXa3o-E6-2-b", width = 300)

with st.expander("Show Maurice's code"):
    st.code(
        '''
import streamlit as st
import streamlit.components.v1 as components

st.title("Hi I'm Maurice")

components.iframe(src="https://www.youtube.com/embed/j1nothJ1_O0?si=8HZwTXa3o-E6-2-b", width = 300)
''', language='python',line_numbers=True
    )