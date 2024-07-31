import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
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
instagram_embed= '''
<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/C9SM_NNv0k_/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/C9SM_NNv0k_/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/C9SM_NNv0k_/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by One Knox Collective (@oneknoxcollective)</a></p></div></blockquote>
<script async src="//www.instagram.com/embed.js"></script>
'''
#components.iframe("https://www.instagram.com/p/C9SM_NNv0k_/embed", width = 300)
components.html(instagram_embed,height=800)
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

st.divider()
st.header("ETFS DATA EXPLORER")
coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
with coach_message:
    st.write("You can change the variables to see the relationship between different metrics!")

#use the Pandas read_csv method to read the gps_data and turn into a dataframe
# Read the CSV file
file_path = './data/last30days_GPS.csv'
all_data = pd.read_csv(file_path)
# Replace ":" with "_" in the column names
all_data.columns = [col.replace(':', ' ') for col in all_data.columns]
#keep only the rows were the column 'Split Name' has a value equal to 'all'
game_data = all_data.loc[all_data['Split Name'] == "game"]
#game_data = game_data.loc[game_data['Tags'] == 'game']
game_data = game_data.set_index('Player Name', drop=False)
game_data["day"] = game_data["Date"] - 45150
game_data = game_data.loc[game_data["day"] > 0]
with st.expander(label="View Your Data",expanded=False):
    #display the uploaded data
    st.write(game_data)
variable_x = st.selectbox("Pick Your X Variable!",game_data.columns.to_list(),1)
variable_y = st.selectbox("Pick Your Y Variable!",game_data.columns.to_list(),8)
variable_size = st.selectbox("Pick Your Size Variable!",game_data.columns.to_list(),9)
if variable_x == 'Session Title':
    chart = alt.Chart(game_data).mark_circle().encode(
    x='Session Title:T',
    y=variable_y,
    size=alt.Size(variable_size,legend=None),
    color=alt.Color('Player Name',legend=None),
    tooltip=["Player Name",]).properties(height=500).interactive()
else:
    chart = alt.Chart(game_data).mark_circle().encode(
    x=variable_x,
    y=variable_y,
    size=alt.Size(variable_size,legend=None),
    color=alt.Color('Player Name',legend=None),
    tooltip=["Player Name","Session Title"]).properties(height=500).interactive()
st.altair_chart(chart, theme="streamlit", use_container_width=True)

