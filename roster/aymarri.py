import streamlit as st

primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

if "number" not in st.session_state:
    st.session_state["number"] = 0


#if st.button("QUIZ TIME"):
st.session_state.number=st.slider("how fast do you think I ran?", 0, 30, st.session_state.number)
st.write("AyMarri ran ", st.session_state.number, "mph")

if st.session_state.number == 13:
    st.write("CORRECT!")

if st.session_state.number >= 30:
    st.write("How generous!, but wrong")

if st.session_state.number == 0:
    st.write("warmer")
    
if st.session_state.number == 1:
    st.write("warmer.")
    
if st.session_state.number == 2:
    st.write("warmer..")
    
if st.session_state.number == 3:
    st.write("warmer...")    
if st.session_state.number == 4:
    st.write("warmer....")    
if st.session_state.number == 5:
    st.write("warmer.....")    
if st.session_state.number == 6:
    st.write("warmer......")    
if st.session_state.number == 7:
    st.write("warmer.......")    
if st.session_state.number == 8:
    st.write("warmer........")    
if st.session_state.number == 9:
    st.write("warmer.........")    
if st.session_state.number == 10:
    st.write("warmer..........")    
if st.session_state.number == 11:
    st.write("warmer............")    
if st.session_state.number == 12:
    st.write("warmer.............")

with st.expander("Show AyMarri's code"):
    st.code(
        body='''
import streamlit as st

primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

if "number" not in st.session_state:
    st.session_state["number"] = 0


#if st.button("QUIZ TIME"):
st.session_state.number=st.slider("how fast do you think I ran?", 0, 30, st.session_state.number)
st.write("AyMarri ran ", st.session_state.number, "mph")

if st.session_state.number == 13:
    st.write("CORRECT!")

if st.session_state.number >= 30:
    st.write("How generous!, but wrong")

if st.session_state.number == 0:
    st.write("warmer")
    
if st.session_state.number == 1:
    st.write("warmer.")
    
if st.session_state.number == 2:
    st.write("warmer..")
    
if st.session_state.number == 3:
    st.write("warmer...")    
if st.session_state.number == 4:
    st.write("warmer....")    
if st.session_state.number == 5:
    st.write("warmer.....")    
if st.session_state.number == 6:
    st.write("warmer......")    
if st.session_state.number == 7:
    st.write("warmer.......")    
if st.session_state.number == 8:
    st.write("warmer........")    
if st.session_state.number == 9:
    st.write("warmer.........")    
if st.session_state.number == 10:
    st.write("warmer..........")    
if st.session_state.number == 11:
    st.write("warmer............")    
if st.session_state.number == 12:
    st.write("warmer.............")
        ''',
        language="python",
        line_numbers=True
    )