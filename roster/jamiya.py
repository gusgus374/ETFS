import streamlit as st
import pandas as pd
import altair as alt
import os
import pathlib
st.title("I am the real Mona")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header(":star:")
if st.button("Jaylen"):
    st.header(":cow:")
if st.button("Mona"):
      st.header(":scales:")
      st.header(":briefcase:")
      st.header(":star_and_crescent:")
      st.header(":libra:")
      st.header(":broken_heart:")
if st.button("Love"):
    st.header("Not Mona")
if st.button("Stop"):
    st.header("Talking to my mom")
    st.header(":octagonal_sign:")
if st.button("zoo"):
    st.header(":monkey:")
if st.button("Elsa"):
    st.write(":cold_face:")
    st.snow()
if st.button("Happy birthday"):
    st.balloons()
if st.button("Taurus"):
     st.header(":taurus:")

     
file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
with open(file_location) as file:
        data = pd.read_csv(file)
ETFS_data = pd.DataFrame(data)
jamiyaData = ETFS_data.loc[ETFS_data["Player Name"] == "Jamiya - ETFS"]
st.dataframe(jamiyaData)
st.write("top speed chart (round to the nearest mph)")


st.line_chart(jamiyaData, x = "Session Title", y="Top Speed (m/s)")

with st.expander("Show Jamiya's code"):
    st.code(
        body='''
import streamlit as st
import altair as alt
import os
import pathlib
st.title("I am the real Mona")

if st. button("Bye Miss Mona!"):
    st.header(":wave:")
if st.button("Me"):
    st.header(":star:")
if st.button("Jaylen"):
    st.header(":cow:")
if st.button("Mona"):
      st.header(":scales:")
      st.header(":briefcase:")
      st.header(":star_and_crescent:")
      st.header(":libra:")
      st.header(":broken_heart:")
if st.button("Love"):
    st.header("Not Mona")
if st.button("Stop"):
    st.header("Talking to my mom")
    st.header(":octagonal_sign:")
if st.button("zoo"):
    st.header(":monkey:")
if st.button("Elsa"):
    st.write(":cold_face:")
    st.snow()
if st.button("Happy birthday"):
    st.balloons()
if st.button("Taurus"):
     st.header(":taurus:")

     
file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
with open(file_location) as file:
        data = pd.read_csv(file)
ETFS_data = pd.DataFrame(data)
jamiyaData = ETFS_data.loc[ETFS_data["Player Name"] == "Jamiya - ETFS"]
st.dataframe(jamiyaData)
st.write("top speed chart (round to the nearest mph)")


st.line_chart(jamiyaData, x = "Session Title", y="Top Speed (m/s)")
        ''',
        language="python",
        line_numbers=True
    )