import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components

st.title("Leo, Ayden, Zane, and Jairus")

file = st.file_uploader("Pick an MP3 file")

st.audio(file)
st.title("Leo, Ayden, Zane, and Jairus")

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

st.header("Our Speed")

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

with open(file_location) as file:
        data = pd.read_csv(file)

ETFS_data = pd.DataFrame(data)

SLIdata = ETFS_data.loc[(ETFS_data["Player Name"] == "Leo - ETFS") | (ETFS_data["Player Name"] == "Ayden - ETFS") | (ETFS_data["Player Name"] == "Zane - ETFS") | (ETFS_data["Player Name"] == "Jairus - ETFS")]
with st.expander("See the dataframe as a table"):
    st.dataframe(SLIdata)

lines = alt.Chart(SLIdata, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)",
        color="Player Name"
)

circles = alt.Chart(SLIdata).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        color="Player Name",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)

combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)

if st.button("Jairus"):
     st.video("./resources/jairus_speed.mp4")

with st.expander("Show Leo and Jamerson's code"):
    st.code(
        body='''
import streamlit as st
import altair as alt

st.title("")

file = st.file_uploader("Pick an MP3 file")

st.audio(file)
st.title("Leo,azyrion,jamerson,Ayden")
        ''',
        language="python",
        line_numbers=True
    )