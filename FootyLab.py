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
    initial_sidebar_state="expanded",
)
st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")
st.title("Welcome to the East Tennessee Freedom Schools footyLab!")

#st.image(image="./resources/profile_coachGus.JPG",width=600)

st.header("This is the home page of our currently-under-development app!")

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


st.subheader("~~Cast some spells~~ Write some python code yourself!")
editor, app= st.columns(2)
INITIAL_CODE = """# write code below!

#try changing the title's name:
st.title("Hello, FootyLab!")

#see what happens when you alter the code below:
some_number = 2
some_text = "I'm a string!"

st.write(some_number)
st.write(some_text)
st.write(some_number + some_number)
"""
with editor:
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
        right = st.container(border=True)
        with right:
             exec(code)