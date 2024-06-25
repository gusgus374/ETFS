import streamlit as st
import altair as alt
if st.button("QUIZ TIME"):
    number=st.slider("how fast do you think I ran?", 0, 15, 30)
    st.write("AyMarri ran ", number, "mph")

    if number == 13:
        st.write("CORRECT!")
    
    if number == 30:
        st.write("How generous!, but wrong")
    
    if number == 0:
        st.write("warmer")
        
    if number == 1:
        st.write("warmer.")
        
    if number == 2:
        st.write("warmer..")
        
    if number == 3:
        st.write("warmer...")    
    if number == 4:
        st.write("warmer....")    
    if number == 5:
        st.write("warmer.....")    
    if number == 6:
        st.write("warmer......")    
    if number == 7:
        st.write("warmer.......")    
    if number == 8:
        st.write("warmer........")    
    if number == 9:
        st.write("warmer.........")    
    if number == 10:
        st.write("warmer..........")    
    if number == 11:
        st.write("warmer............")    
    if number == 12:
        st.write("warmer.............")