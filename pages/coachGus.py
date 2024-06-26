import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
import streamlit.components.v1 as components
from streamlit_ace import st_ace

st.image(image="./resources/ETSF_logo.png",width=60)
st.title("Welcome to the East Tennessee Freedom Schools footyLab!")

if st.button("Best ever"):
      st.image("https://www.si.com/.image/t_share/MTc5NTMwMzAxNjQ1NTMwMjQ5/gettyimages-891445.jpg")

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