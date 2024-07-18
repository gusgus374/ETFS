import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
#import time 
import os
import pathlib
import streamlit.components.v1 as components

def plotbox(df):
    domain = ['Green', "Blue", "Red"]
    range_ = ['chartreuse', 'blue', 'red']
    range_g = ['chartreuse', 'chartreuse','chartreuse']
    range_b = ['blue', 'blue', 'blue']
    df = df.groupby(["Team"],as_index=False).value_counts()
    d = alt.Chart(df).mark_bar(opacity=0.2).encode(
        y = alt.Y("Green Votes:Q"),
        x = alt.X("Name:N").title("Players by Team").sort(),
        #y2 = alt.Y2("Blue Votes:Q"),
        #y3 = alt.Y("Total votes:Q"),
        color = alt.Color("Team:N",legend=None).scale(domain=domain,range=range_g),
        #row=alt.Row("Name:N"),
        #column = alt.Column("Name:N"),
        tooltip=["Name", "Team", "Blue Votes","Green Votes"]
    ).interactive()
    e = alt.Chart(df).mark_bar(opacity=0.35).encode(
        y = alt.Y("Blue Votes:Q"),
        x = alt.X("Name:N").title(None).sort(),
        #y2 = alt.Y2("Blue Votes:Q"),
        #y3 = alt.Y("Total votes:Q"),
        color = alt.Color("Team:N",legend=None).scale(domain=domain,range=range_b),
        #row=alt.Row("Name:N"),
        #column = alt.Column("Name:N"),
        tooltip=["Name", "Team", "Blue Votes","Green Votes"]
    ).interactive()
    f = alt.Chart(df).mark_bar(opacity=0.55).encode(
        y = alt.Y("Total votes:Q").title("Total Votes"),
        x = alt.X("Name:N").title(None).sort(),
        #y2 = alt.Y2("Blue Votes:Q"),
        #x2 = alt.X2("Name:N"),
        #y2 = alt.Y2("Blue Votes:Q"),
        #y3 = alt.Y("Total votes:Q"),
        color = alt.Color("Team:N",legend=None).scale(domain=domain,range=range_),
        #row=alt.Row("Name:N"),
        #column = alt.Column("Name:N"),
        tooltip=["Name", "Team", "Blue Votes","Green Votes"]
    ).properties(height=500).interactive()
    #st.altair_chart(c, use_container_width=True)

    return f+e+d
#st.title("NEW TEAMS FOR TUESDAY JUNE 18th.")
st.warning("Do you have a video clip highlight on your page? Must use an mp4 file!", icon="❓")
st.warning("Do you have a graph showing some data over time on your page?", icon="❓")
st.warning("Do you have something unique to you on your page?", icon="❓")
st.title("CLASS PAGE - example for finale")
st.code('''
st.title("CLASS PAGE - example for finale")
        ''')
#Power Play
blueTeam1 = ["Azy'rion","AyMarri","Ayden","Dalton","Jamerson","Garrett","Jamiya","Jarius","Zane","Raye","Nevaeh","Ronnie"]
greenTeam1 = ["AyNirra","Elias","Elhaj","Ceslee","Imani","Michaya","Gabi","Samantha"]

#speed distance power
blueTeam2 = ["Azy'rion","Mr.Josh","Ms.Mona","Jarius","Jamiya","Ronnie","Gabby","Aynira","Ayden","Ceslee","Michaya"]
greenTeam2 = ["Mr. Jaylen","Eli","Samantha","Elhaj","Imani","Leo","Breionna","Maurice","Dalton","Garrett","Nevaeh"]

#same teams
#[""]
#[""]

#Power Play
blueTeam3 = ["Jimaya","Michaya","Samantha","Leo","Ceslee","Azy'rion","Nevaeh","Raye"]
greenTeam3 = ["Ronnie","Dalton","Breionna","Ms.Mona","Maurice","Jairus","Garrett","Zane"]

#based on distance
blueTeam4 = ["Mr. Josh","Ronnie","Azy'rion","Ayden","Michaya","Jarius","Nevaeh","Zane"]
greenTeam4 = ["Leo","Samantha","Dalton","Olivia","Garrett","Imani","Ceslee"]

#based on play, distance, energy
greenTeam5 = ["Ronnie","Mr.Josh","Azaryion","Jairus","Ms.Mona","Dalton","Garrett"]
blueTeam5 = ["Ayden","Maurice","Elhaj","Nevaeh","Zane","Elias","Leo"]

#speed
blueTeam6 = ["Aynira","Ceslee","Ronnie","Jimaya","Gabby","Imani","Mr. Josh", "Samantha","Ms.Mona","Josh"]
greenTeam6 = "Leo","Maurice","Neveah","Elhaj","Jarius","Dalton","Garrett","Jamerson","Elias","mr. Jalen"

#speed & distance

blueTeam7 = ["Ronnie","Michya","Azy'rion","Ayden","Jamiya","Jamerson","Gabby","Imani","Jairus"]
greenTeam7 = ["Breionna","Leo","Garrett","Neveah","Dalton","Maurice","Zane","Aynira","Olivia","Ceslee"]

#Top Speed
blueTeam8 = ["AyNarri","Aynira","Elias","Dalton","Jamerson","Jamiya","Jarius","Ronnie","Samantha","Nevaeh",""]
greenTeam8 = ["Azy'rion","Ayden","Elhaj","Ceslee","Imani","Michaya","Garrett","Olivia","Zane","Raye","Leo"]


players = [["Ayden",1,1],["AyMarri",1,1],["Aynira",1,1],["Azy'rion",1,1],["Breionna",1,1],["Ceslee",1,1],["Dalton",1,1],["Elhaj",1,1],["Elias",1,1],["Garrett",1,1],["Imani",1,1],["Jairus",1,1],["Jamerson",1,1],["Jamiya",1,1],["Joseph",1,1],["Leo",1,1],["Maurice",1,1],["Michya",1,1],["Nevaeh",1,1],["Olivia",1,1],["Raye",1,1],["Ronnie",1,1],["Samantha",1,1],["Zane",1,1]]
df = pd.DataFrame(players,columns=["Name","Green Votes","Blue Votes"])
#st.dataframe(df)
df["Team"] = pd.Series()
df["Total votes"] = pd.Series()
#chartbox = st.container(height=500,border=False)
#chartbox2 = st.container()
#barchart = st.bar_chart(df,x="Name",y="Total votes")
#barchart.add_rows(df)
#df = df.groupby(["Team"],as_index=False).value_counts()
plot = st.empty()
for i,r in df.iterrows():
    if r["Name"] in blueTeam1:
        #st.write(r["Name"],r["Blue Votes"])
        #st.write(df.at[i,"Blue Votes"])
        df.at[i,"Blue Votes"]  += + 1
        #st.write(df.at[i,"Blue Votes"])
    if r["Name"] in greenTeam1:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam2:
        df.at[i,"Blue Votes"] += 1
        #st.write(df.at[i,"Blue Votes"])
    if r["Name"] in greenTeam2:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam3:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam3:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam4:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam4:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam5:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam5:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam6:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam6:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam7:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam7:
        df.at[i,"Green Votes"] += 1
    if r["Name"] in blueTeam8:
        df.at[i,"Blue Votes"] += 1
    if r["Name"] in greenTeam8:
        df.at[i,"Green Votes"] += 1
    #st.write(df)

    for j,rr in df.iterrows():
        if rr["Blue Votes"] > rr["Green Votes"]:
            df.at[j,"Team"] = "Blue"
        elif rr["Green Votes"] > rr["Blue Votes"]:
            df.at[j,"Team"] = "Green"
        else:
            df.at[j,"Team"] = "Red"
        df.at[j,"Total votes"] = rr["Blue Votes"] + rr["Green Votes"]
        #layers = plotbox(df)
    #plot.altair_chart(layers,use_container_width=True)
st.header("Python Libraries used:")
st.code('''
import streamlit as st
import pandas as pd
import os
import pathlib
import altair as alt
import streamlit.components.v1 as components
        ''')
if st.button('Joseph "Slipped"'):
    st.video("./resources/josephslipped.mp4")
st.code('''
if st.button('Joseph "Slipped"'):
    st.video("./resources/josephslipped.mp4")
        ''')

#uploaded_file = st.file_uploader("Choose a data file")
#if uploaded_file is not None:
        # use the Pandas read_csv method to read the gps_data and turn into a dataframe
#        all_data = pd.read_csv(uploaded_file)
        # keep only the rows were the column 'Split Name' has a value equal to 'all'
 #       game_data = all_data.loc[all_data['Split Name'] == "game"]
        #game_data = game_data.loc[game_data['Tags'] == 'game']
  #      game_data = game_data.set_index('Player Name', drop=False)
        #game_data["day"] = game_data["Date"] - 45150
        #game_data = game_data.loc[game_data["day"] > 0]
   #     with st.expander(label="View Your Data",expanded=False):
                #display the uploaded data
    #            st.write(game_data)
     #   variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
      #  variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
       # variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
#if uploaded_file is not None:
 #   chart = alt.Chart(game_data).mark_circle().encode(
  #      x=variable_x,
   #     y=variable_y,
    #    size=alt.Size(variable_size,legend=None),
     #   color=alt.Color('Player Name',legend=None),
      #  tooltip=["Player Name","Session Title",]).properties(height=500).interactive()
    #st.altair_chart(chart, theme="streamlit", use_container_width=True)
with st.echo("below"):
    st.header("Graph example")

    file_location = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')

    with open(file_location) as file:
            data = pd.read_csv(file)

    ETFS_data = pd.DataFrame(data)

    SLIdata = ETFS_data.loc[(ETFS_data["Player Name"] == "Mr. Josh - ETFS") | (ETFS_data["Player Name"] == "Ms. Mona - ETFS") | (ETFS_data["Player Name"] == "Mr. Jaylen - ETFS")]
    with st.expander("See the dataframe as a table"):
        st.dataframe(SLIdata)

    lines = alt.Chart(SLIdata, title="My interactive chart").mark_line().encode(
            x="Session Title:T",#the little ":T" after "Session Title" tells altair that this data is a time or date value
            y="Top Speed (m/s)",
            color="Player Name"
    )

    circles = alt.Chart(SLIdata).mark_circle().encode(
            x="Session Title:T",
            y="Top Speed (m/s)",
            color="Player Name",
            size=alt.Size("Distance (km)",legend=None),
            tooltip=["Player Name","Session Title","Top Speed (m/s)", "Split Name", "Distance (km)"]
    )

    combined_chart = (lines + circles).interactive()
    st.altair_chart(combined_chart, use_container_width=True)

st.header("_Something Unique_")
with st.echo("below"):
    st.header("Soccer... and Data... *and* Science?")
    st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
    st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
    st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

    col1, col2 = st.columns(2)
    col1.write("They used their knowledge of charged particles and electric fields:")
    col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
    with col2:
            iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
            components.iframe(iframe_src2,600,500)

    with col1:
            iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
            components.iframe(iframe_src,height=500)
            st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
    st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
    st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
    st.subheader("or")
    st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')
