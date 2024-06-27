import streamlit as st
import altair as alt
import time 
st.title("Five below commercial")

if st.button("Click Me For An Awesomely Icy Deal"):
    st.snow()
    
    st.title("YOU HAVE ONE MINUTE.")
    #st.set_page_config()

ph = st.empty()
N = 1*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)

with st.expander("Show Raye's code"):
    st.code(
        body='''
import streamlit as st
import altair as alt
import time 
st.title("Five below commercial")

if st.button("Click Me For An Awesomely Icy Deal"):
    st.snow()
    
    st.title("YOU HAVE ONE MINUTE.")
    #st.set_page_config()

ph = st.empty()
N = 1*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)
        ''',
        language="python",
        line_numbers=True
    )
