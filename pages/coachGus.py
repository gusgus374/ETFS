import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FootyLab codeBox",
    page_icon="./resources/DR_favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")
st.title("Your Brain, Electricity, Some Stuff Called 'Myelin', and Getting Better at Stuff")
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