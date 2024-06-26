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

if "user" not in st.session_state:
    st.session_state.user = None
#if "password" not in st.session_state:
#     st.session_state.password = None

ROLES = [None, "Ayden", "AyMarri","Aynira","Azy'rion","Breionna","Ceslee","Dalton","Elhaj","Elias","Garrett","Imani","Jairus","Jamiya","Joseph","Leo","Maurice","Michya","Nevaeh","Olivia","Raye","Ronnie","Samantha","Zane","Gus","Admin","Mrs. Summey"]
allroles = ["Ayden", "AyMarri","Aynira","Azy'rion","Breionna","Ceslee","Dalton","Elhaj","Elias","Garrett","Imani","Jairus","Jamiya","Joseph","Leo","Maurice","Michya","Nevaeh","Olivia","Raye","Ronnie","Samantha","Zane","Gus","Mrs. Summey","Admin"]
playersdeployed = ["Ayden", "AyMarri","Azy'rion","Breionna","Elias","Jamiya","Leo","Samantha","Gus"]
def login():

    st.header("Log in")
    user = st.selectbox("User", ROLES)
    #password = st.text_input("Password")

    if st.button("Log in"):
        st.session_state.user = user
        #st.session_state.password = password
        st.rerun()


def logout():
    st.session_state.user = None
    #st.session_state.password = None
    st.rerun()


user = st.session_state.user
#password = st.session_state.password

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

BootRoom = st.Page(
    "./pages/1_BootRoom.py",
    title="BootRoom",
    icon=":material/help:",
    default=(user == "Admin"),
)
coachGus = st.Page(
    "./pages/coachGus.py", title="Coach's Examples", icon=":material/bug_report:",default=(user == "Gus")
)
classpage = st.Page(
    "./pages/Class_Page.py",
    title="Class Page",
    icon=":material/healing:",
)
codeBox = st.Page(
    "./pages/codeBox.py", title="", icon=":material/handyman:",default=(user not in playersdeployed)
)
prosoccer = st.Page(
    "./pages/2_US_Pro_Soccer.py",
    title="Pro Soccer Data",
    icon=":material/person_add:",
)
ayden = st.Page("./roster/LeoJamersonAydenAzyrion.py", title="Music Boys", icon=":material/security:",default=(user=="Ayden" or user == "Leo" or user == "Azy'rion" or user == "Jamerson"))

samantha = st.Page("./roster/samantha.py", title="Samantha", icon=":material/security:",default=(user=="Samantha"))

aymarri = st.Page("./roster/aymarri.py", title="AyMarri", icon=":material/security:",default=(user=="AyMarri"))

breionna = st.Page("./roster/breionna.py", title="Breionna", icon=":material/security:",default=(user=="Breionna"))

jamiya = st.Page("./roster/jamiya.py", title="Jamiya", icon=":material/security:",default=(user=="Jamiya"))

eli = st.Page("./roster/eli.py", title="Eli", icon=":material/security:",default=(user=="Elias"))

account_pages = [logout_page, settings]
explore_pages = [BootRoom, prosoccer]
build_pages = [codeBox, coachGus]
deployed_pages = [classpage, ayden, samantha, aymarri, breionna, jamiya, eli]

page_dict = {}
if (st.session_state.user in allroles):
    page_dict["Explore"] = explore_pages
if (st.session_state.user in allroles):
    page_dict["Build"] = build_pages
if (st.session_state.user in playersdeployed):
    page_dict["Deployed"] = deployed_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

st.logo("./resources/footyLab_v2_96_NB.png",link="https://datarook.com/")

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
      