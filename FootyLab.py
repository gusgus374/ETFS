import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
from streamlit_ace import st_ace
import streamlit.components.v1 as components
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns

st.set_page_config(
    page_title="footyLab • Play to Learn | DataRook, Inc.",
    page_icon="./resources/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.sidebar.page_link("FootyLab.py", label=":seedling: Home Page ")
st.sidebar.page_link("pages/1_BootRoom.py", label=":star: Boot Room ")
st.sidebar.page_link("pages/codeBox.py", label=":computer: CODE BOX ")
st.sidebar.page_link("pages/coachGus.py", label=":pushpin: Coach's Examples ")
st.sidebar.page_link("pages/Class_Page.py", label=":bar_chart: Class Page")
st.sidebar.page_link("pages/2_US_Pro_Soccer.py", label=":earth_americas: Pro Soccer Data :soccer:",disabled=False)
st.sidebar.page_link("pages/test.py", label="test",disabled=False)
st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")

st.image(image="./resources/ETSF_logo.png",width=60)
st.title("Welcome to the East Tennessee Freedom Schools footyLab!")



st.header("This is the home page of our app!")

#st.text("This is the home page of our currently-under-development app!")
st.text("The goal is for us to explore the data we have been collecting on the soccer field right here in the footyLab.")
st.subheader("BUT HOW ARE WE GONNA DO THIS?!")
st.markdown("Magic. Well... actually by writing some *python code*... which feels like magic, I promise.")

st.header("Hacking Skills = ~Computer Programming~ *Magic*")
iframe_src2 = "https://www.youtube.com/embed/Qgr4dcsY-60?si=gsK8I_rpz0cpH5UO"
components.iframe(iframe_src2,400,300)

coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Now I'm going to ``cast a spell`` (:wink:) to generate a button:")

st.code("""
        #this spell is actually just python code
st.button("I'm a Button")
        """)
st.button("I'm a Button")

coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Okay cool! We can click on our newly casted button but... that's about it. Let's try a slightly more advanced spell:")

st.code("""
if st.button("Click me for a celebration"):
        st.balloons()
        """)

if st.button("Click me for a celebration"):
        st.balloons()

st.subheader("See? Magic.")
st.divider()
coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Below you'll find the *codeBox* where you can try coding yourself!")



editor, app= st.columns(2)
INITIAL_CODE = """#try changing the title's name:
st.title("Hello, FootyLab!")

#see what happens when you alter the code below:
some_number = 2
some_text = "I'm a string!"

st.write(some_number)

st.header(some_text)

st.write(some_number + some_number)
"""
with editor:
    st.subheader("~~Cast some spells~~ Write some python code yourself!")
    left = st.container(border=True)
    with left:
         code = st_ace(
              value=INITIAL_CODE,
              language="python",
              placeholder="st.header('Hello world!')",
              theme="tomorrow_night_eighties",
              show_gutter=True,
              show_print_margin=True,
              auto_update=False,
              min_lines=16,
              readonly=False,
              key="ace-editor",
              )
         #st.write("Hit `CTRL+ENTER` to refresh")
         #st.write("*Remember to save your code separately!*")
st.divider()

with app:
        st.subheader("Your Results :point_down:")
        right = st.container(border=True)
        with right:
             exec(code)
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
      