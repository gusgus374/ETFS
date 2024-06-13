import streamlit as st

from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace

import pandas as pd
import numpy as np
import altair as alt
st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")

st.set_page_config(
    page_title="FootyLab codeBox",
    page_icon="./resources/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("FootyLab codeBox")


coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Below you'll find a *file uploader* and the *codeBox* where you can play around with data you upload!")
with st.echo():
     uploaded_file = st.file_uploader("Choose a data file")
     if uploaded_file is not None:
        # use the Pandas read_csv method to read the gps_data and turn into a dataframe
        all_data = pd.read_csv(uploaded_file)
        # keep only the rows were the column 'Split Name' has a value equal to 'all'
        game_data = all_data.loc[all_data['Split Name'] == 'all']
        game_data = game_data.set_index('Player Name', drop=False)
        with st.expander(label="View Your Data",expanded=False):
            #display the uploaded data
            st.write(game_data)
        variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
        variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
        variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)

editor = st.container(border=True)
INITIAL_CODE = """# write code below!
if uploaded_file is not None:
    chart = alt.Chart(game_data).mark_circle().encode(
        x=variable_x,
        y=variable_y,
        size=alt.Size(variable_size,legend=None),
        color=alt.Color('Player Name',legend=None),
        tooltip=["Player Name","Session Title",]).properties(height=500).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
"""

with editor:
    code = st_ace(
        value=INITIAL_CODE,
        language="python",
        placeholder="st.header('Hello world!')",
        theme="tomorrow_night_eighties",
        show_gutter=True,
        show_print_margin=True,
        auto_update=False,
        readonly=False,
        key="ace-editor",
    )
    st.write("Hit `CTRL+ENTER` to refresh")
    #st.write("*Remember to save your code separately!*")

st.header("*Your Result:*")
app = st.container(border=True)
with app:
    exec(code)