import streamlit as st

st.title("")
import altair as alt
import time 

start_time = time.time()
st.write(start_time)
st.title("Five below commercial")

with st.expander("Click Me For An Awesomely Icy Deal"):
    #st.snow()
    correct = "solved"
    st.title("SOLVE THIS RIDDLE OR ELSE")
    st.header("you have one minute")
    st.subheader("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I?")
    answer = st.text_input("WRITE YOUR ANSWER")
    
    if answer == correct:
        answer_time = time.time()
        time_to_answer = answer_time - start_time
        st.write("it took you ",time_to_answer,"seconds to figure it out")
        st.write(":trophy:")
    if answer != correct:
        st.write("WRONG")
    
    #st.set_page_config()

ph = st.empty()
N = 1*60
#for secs in range(N,0,-1):
#    mm, ss = secs//60, secs%60
#    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#    time.sleep(1)

with st.expander("Show Raye's code"):
    st.code(
        body='''
import streamlit as st

st.title("")
import altair as alt
import time 

start_time = time.time()
st.write(start_time)
st.title("Five below commercial")

with st.expander("Click Me For An Awesomely Icy Deal"):
    #st.snow()
    correct = "solved"
    st.title("SOLVE THIS RIDDLE OR ELSE")
    st.header("you have one minute")
    st.subheader("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I?")
    answer = st.text_input("WRITE YOUR ANSWER")
    
    if answer == correct:
        answer_time = time.time()
        time_to_answer = answer_time - start_time
        st.write("it took you ",time_to_answer,"seconds to figure it out")
        st.write(":trophy:")
    if answer != correct:
        st.write("WRONG")
    
    #st.set_page_config()

ph = st.empty()
N = 1*60
#for secs in range(N,0,-1):
#    mm, ss = secs//60, secs%60
#    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#    time.sleep(1)
        ''',
        language="python",
        line_numbers=True
    )
