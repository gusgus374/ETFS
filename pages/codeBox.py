import streamlit as st

from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace

import pandas as pd
import numpy as np
import altair as alt
import os
from pathlib import Path


if 'code' not in st.session_state:
     st.session_state['code'] = None
if 'old_code' not in st.session_state:
     st.session_state['old_code'] = None

st.title("footyLab codeBox")
with st.sidebar:
    file = st.file_uploader("upload python script",type=[".py"])

if st.session_state.old_code is not None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        if st.session_state.old_code != decoded_string:
            st.session_state.old_code = decoded_string
        st.session_state.code = st.session_state.old_code
    else:
        st.session_state.code = st.session_state.old_code

if st.session_state.old_code is None:
    if file is not None:
        old_code = file.read()
        decoded_string = old_code.decode("utf-8")
        st.session_state.old_code = decoded_string
        INITIAL_CODE = st.session_state.old_code
            
    else:
        INITIAL_CODE = """# write code below!
import streamlit as st

st.title("What do you want to build today?")

                            """
     

tab1, tab2 = st.tabs(["EDITOR","USER EXPERIENCE"])



with tab1:
    editor = st.container(border=True)
    if st.session_state.code is None:
        with editor:
            code = st_ace(
                value=INITIAL_CODE,
                language="python",
                placeholder="st.header('Hello world!')",
                theme="tomorrow_night_eighties",
                show_gutter=True,
                wrap=True,
                show_print_margin=True,
                auto_update=False,
                readonly=False,
                key="ace-editor",
            )
            st.write("Hit `CTRL+ENTER` to refresh")
    if st.session_state.code is not None:
        with editor:
            code = st_ace(
                value=st.session_state.code,
                language="python",
                placeholder="st.header('Hello world!')",
                theme="tomorrow_night_eighties",
                show_gutter=True,
                wrap=True,
                show_print_margin=True,
                auto_update=False,
                readonly=False,
                key="ace-editor",
            )

st.session_state.code = code
st.session_state.old_code = st.session_state.code
        #st.write("*Remember to save your code separately!*")



with tab2:
    app = st.container(border=True)
    with app:
        exec(st.session_state.code)

with st.popover("SAVE YOUR WORK"):
    file_name = st.text_input("Name your file",f"{st.session_state.user}")
    btn = st.download_button(
                    label="Download Python File",
                    data = code,
                    file_name=f"{file_name}.py"
    )
