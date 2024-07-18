import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components

st.title("East Tennessee Freedom Schools")

st.header("Hi I'm Elhaj and I like basketball and soccer.")

if st.button("Soccer dice game"):
    st.image("./resources/IMG_4749.jpeg")