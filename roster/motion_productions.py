import streamlit as st
import pandas as pd
import altair as alt
import os
import pathlib

st.title("Hi, we're Motion Productions")
if st.button("Balloons!"):
    st.balloons()
    st.snow()
    st.write("Joseph and Ronnie's data")
    st.write(":heavy_dollar_sign:")
    st.write(":fire:")
    st.write(":moneybag:")


file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

with open(file_location) as file:
        data = pd.read_csv(file)

ETFS_data = pd.DataFrame(data)

#st.dataframe(ETFS_data)

mpData = ETFS_data.loc[(ETFS_data["Player Name"] == "Joseph - ETFS") | (ETFS_data["Player Name"] == "Ronnie - ETFS") | (ETFS_data["Player Name"] == "Maurice - ETFS") | (ETFS_data["Player Name"] == "Jamerson - ETFS")]

with st.expander("See the dataframe as a table"):
    st.dataframe(mpData)

lines = alt.Chart(mpData, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)",
        color="Player Name"
)

circles = alt.Chart(mpData).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        color="Player Name",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)
combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)

if st.button("Ronnie's Highlight"):
     st.video("./resources/ronnie_goal.mp4")

with st.expander("Show Joseph & Ronnie's code"):
    st.code(
        '''
import streamlit as st
import altair as alt
import os
import pathlib

st.title("Hi, we're Motion Productions")
if st.button("Balloons!"):
    st.balloons()
    st.snow()
    st.write("Joseph and Ronnie's data")
    st.write(":heavy_dollar_sign:")
    st.write(":fire:")
    st.write(":moneybag:")

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

with open(file_location) as file:
        data = pd.read_csv(file)

ETFS_data = pd.DataFrame(data)

#st.dataframe(ETFS_data)

mpData = ETFS_data.loc[(ETFS_data["Player Name"] == "Joseph - ETFS") | (ETFS_data["Player Name"] == "Ronnie - ETFS") | (ETFS_data["Player Name"] == "Maurice - ETFS") | (ETFS_data["Player Name"] == "Jamerson - ETFS")]

with st.expander("See the dataframe as a table"):
    st.dataframe(mpData)

lines = alt.Chart(mpData, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)",
        color="Player Name"
)

circles = alt.Chart(mpData).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        color="Player Name",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)
combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)

''', language='python',line_numbers=True
    )