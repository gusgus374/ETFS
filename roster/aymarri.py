import pandas as pd
import os
import pathlib
import streamlit as st

st.title("Welcome to AyMarri's Page!")

st.subheader("to view my data just scroll down")
st.caption("make sure to do your research...")
if st.button("Yay!"):
    st.balloons()
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
with open(file_location) as file:
        data = pd.read_csv(file)
ETFS_data = pd.DataFrame(data)
aymarriData = ETFS_data.loc[ETFS_data["Player Name"] == "AyMarri - ETFS"]
st.dataframe(aymarriData)

st.write("top speed chart (round to the nearest mph)")


st.line_chart(aymarriData, x = "Session Title", y="Top Speed (m/s)")

st.title("POP QUIZ!")

if "number" not in st.session_state:
    st.session_state["number"] = 0
#if st.button("QUIZ TIME"):
st.session_state.number=st.slider("1.   what was my top speed?", 0, 30, st.session_state.number)
if st.button('click for a hint'):
    st.caption('multiply 5.8 and 2.23 and round up')
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
answer = st.session_state.number
if answer == 13:
    st.write("CORRECT")



st.write('2.   how many power plays did I have on date 45,468?')

with st.expander("Show AyMarri's code"):
    st.code(
        body='''
import pandas as pd
import os
import pathlib
import streamlit as st

st.title("Welcome to AyMarri's Page!")

st.subheader("to view my data just scroll down")
st.caption("make sure to do your research...")
if st.button("Yay!"):
    st.balloons()
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
with open(file_location) as file:
        data = pd.read_csv(file)
ETFS_data = pd.DataFrame(data)
aymarriData = ETFS_data.loc[ETFS_data["Player Name"] == "AyMarri - ETFS"]
st.dataframe(aymarriData)

st.write("top speed chart (round to the nearest mph)")


st.line_chart(aymarriData, x = "Session Title", y="Top Speed (m/s)")

st.title("POP QUIZ!")

if "number" not in st.session_state:
    st.session_state["number"] = 0
#if st.button("QUIZ TIME"):
st.session_state.number=st.slider("1.   what was my top speed?", 0, 30, st.session_state.number)
if st.button('click for a hint'):
    st.caption('multiply 5.8 and 2.23 and round up')
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
answer = st.session_state.number
if answer == 13:
    st.write("CORRECT")



st.write('2.   how many power plays did I have on date 45,468?')
        ''',
        language="python",
        line_numbers=True
    )