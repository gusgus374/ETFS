import streamlit as st
import pandas as pd
import altair as alt
import os
import pathlib

st.title("Hi, were Motion Productions")
if st.button("Balloons"):
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

st.dataframe(ETFS_data)

with st.expander("Show Joseph & Ronnie's code"):
    st.code(
        '''
import streamlit as st
import altair as alt
import os
import pathlib

st.title("Hi, were Motion Productions")
if st.button("Balloons"):
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

st.dataframe(ETFS_data)

''', language='python',line_numbers=True
    )