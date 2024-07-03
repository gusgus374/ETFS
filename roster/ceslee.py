import streamlit as st

st.title("What do you want to build today?")

                            
st.snow()

with st.expander("Show Ceecee's code"):
    st.code(
        body='''
import streamlit as st

st.title("What do you want to build today?")

                            
st.snow()
        ''',
        language="python",
        line_numbers=True
    )