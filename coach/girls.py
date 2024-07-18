import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components

tab1, tab2, tab3, tab4 = st.tabs(["Neveah", "Bre", "Raye", "Cece"])

if st.button("Highlight"):
    st.video("./resources/Raye_Jamiya_Defense.mp4")

