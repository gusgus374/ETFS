import streamlit as st

st.title("What do you want to build today?")

if st.button("balloons"):
    import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

with st.expander("Show Ayden's code"):
    st.code(
        '''
import streamlit as st

st.title("What do you want to build today?")

if st.button("balloons"):
    import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()
''', language='python',line_numbers=True
    )