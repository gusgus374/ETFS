import streamlit as st
import altair as alt
import pandas as pd
import altair as alt
import os
import pathlib

st.title("What do you want to build today?")

st.snow()

if st. button("Bye Mr. Jaylen.!"):
    st.header(":cockroach:")
if st.button(":tm:"):
    st.header(":mammoth:")
if st.button("Jaylen"):
    st.header(":monkey:")
    
#def cook_breakfast():
 #   msg = st.toast('Gathering ingredients...')
  #  time.sleep(1)
   # msg.toast('Cooking...')
    #time.sleep(1)
    #msg.toast('Ready!', icon = "🥞")

#if st.button('Cook breakfast'):
 #   cook_breakfast()


st.header("ceslee")

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

with open(file_location) as file:
    data = pd.read_csv(file)

ETFS_data = pd.DataFrame(data)

CeeCee_data = ETFS_data.loc[(ETFS_data["Player Name"] == "Ceslee - ETFS")]

with st.expander("See the dataframe as a table"):
    st.dataframe(CeeCee_data)

lines = alt.Chart(CeeCee_data, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)"
)

circles = alt.Chart(CeeCee_data).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)

combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)

with st.expander("Show Ceecee's code"):
    st.code(
        body='''
import streamlit as st
import altair as alt
import pandas as pd
import os
import pathlib

st.title("What do you want to build today?")

st.snow()

if st. button("Bye Mr. Jaylen.!"):
    st.header(":cockroach:")
if st.button(":tm:"):
    st.header(":mammoth:")
if st.button("Jaylen"):
    st.header(":monkey:")
    
#def cook_breakfast():
 #   msg = st.toast('Gathering ingredients...')
  #  time.sleep(1)
   # msg.toast('Cooking...')
    #time.sleep(1)
    #msg.toast('Ready!', icon = "🥞")

#if st.button('Cook breakfast'):
 #   cook_breakfast()


st.header("ceslee")

file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

with open(file_location) as file:
    data = pd.read_csv(file)

ETFS_data = pd.DataFrame(data)

CeeCee_data = ETFS_data.loc[(ETFS_data["Player Name"] == "Ceslee - ETFS")]

with st.expander("See the dataframe as a table"):
    st.dataframe(CeeCee_data)

lines = alt.Chart(CeeCee_data, title="My interactive chart").mark_line().encode(
        x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
        y="Top Speed (m/s)"
)

circles = alt.Chart(CeeCee_data).mark_circle().encode(
        x="Session Title:T",
        y="Top Speed (m/s)",
        size=alt.Size("Distance (km)",legend=None),
        tooltip=["Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
)

combined_chart = (lines + circles).interactive()
st.altair_chart(combined_chart, use_container_width=True)
        ''',
        language="python",
        line_numbers=True
    )