import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
import streamlit.components.v1 as components

st.set_page_config(
    page_title="code examples",
    page_icon="./resources/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.sidebar.page_link("FootyLab.py", label=":seedling: Home Page ")
st.sidebar.page_link("pages/1_BootRoom.py", label=":star: Boot Room ")
st.sidebar.page_link("pages/codeBox.py", label=":computer: CODE BOX ")
st.sidebar.page_link("pages/coachGus.py", label=":pushpin: Coach's Examples ")
st.sidebar.page_link("pages/Class_Page.py", label=":bar_chart: Class Page ")
st.sidebar.page_link("pages/2_US_Pro_Soccer.py", label=":earth_americas: Pro Soccer Data :soccer:",disabled=False)
with st.sidebar:
    st.divider()
st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")
st.title("Your Brain, Electricity, Some Stuff Called 'Myelin', and Getting Better at Stuff.")
col1, col2 = st.columns(2)
with col2:
        st.image(image="./resources/myelin_sheath.jpg",width=400)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/resistance-in-a-wire/latest/resistance-in-a-wire_en.html"
        components.iframe(iframe_src,height=500)

st.header("Soccer... and Data... *and* Science?")
st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

col1, col2 = st.columns(2)
col1.write("They used their knowledge of this:")
col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
with col2:
        iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
        components.iframe(iframe_src2,600,500)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
        components.iframe(iframe_src,height=500)
        st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
st.subheader("Soccer and Science.")
st.header("What about that data thing? What *is* data?")

st.divider()
st.header("Links and Resources")
col1, col2 = st.columns(2)
with col1:
      #st.subheader("Streamlit ~~Docs~~ Spellbook")
      st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about Streamlit ~~methods~~ spells", icon="🪄")
      uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
      with open(uploaded_file) as f:
            btn = st.download_button(
                  label="Download Last 30 Days GPS Data",
                  data = f,
                  file_name="gps_data.csv",
                  mime="text/csv"
                )
with col2:
      st.page_link("https://oneknoxcollective.notion.site/ETFS-Soccer-Scientists-8d132bcda49c4385b0a5c41adef5ebb8?pvs=4", label="ETFS Soccer Scientist Home Page", icon="🏡")

coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Below you'll find a *file uploader* and the *codeBox* where you can play around with data you upload!")
with st.echo():
     uploaded_file = st.file_uploader("Choose a data file")
     if uploaded_file is not None:
        # use the Pandas read_csv method to read the gps_data and turn into a dataframe
        all_data = pd.read_csv(uploaded_file)
        # keep only the rows were the column 'Split Name' has a value equal to 'all'
        game_data = all_data.loc[all_data['Split Name'] == "game"]
        #game_data = game_data.loc[game_data['Tags'] == 'game']
        game_data = game_data.set_index('Player Name', drop=False)
        #game_data["day"] = game_data["Date"] - 45150
        #game_data = game_data.loc[game_data["day"] > 0]
        with st.expander(label="View Your Data",expanded=False):
            #display the uploaded data
            st.write(game_data)
        variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
        variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
        variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
if uploaded_file is not None:
    chart = alt.Chart(game_data).mark_circle().encode(
        x=variable_x,
        y=variable_y,
        size=alt.Size(variable_size,legend=None),
        color=alt.Color('Player Name',legend=None),
        tooltip=["Player Name","Session Title",]).properties(height=500).interactive()
    st.altair_chart(chart, theme="streamlit", use_container_width=True)