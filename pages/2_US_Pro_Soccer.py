import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import Sbopen, Pitch
import statsmodels.api as sm
import statsmodels.formula.api as smf
from matplotlib import colors
from itscalledsoccer.client import AmericanSoccerAnalysis
import os
import pathlib
from scipy import stats
from mplsoccer import PyPizza, FontManager
import streamlit as st
import ast
import seaborn as sns
#import folium
#from folium.plugins import HeatMap
import altair as alt

# Helper function to get the values from the list of dictionaries
def get_value_from_data(data, action_type, key):
    for item in data:
        if item['action_type'] == action_type:
            return item.get(key, None)
    return None
leagues = ["nwsl","mls","uslc","usl1","mlsnp"]
with st.sidebar:
    with st.popover("Select league"):
        league = st.selectbox("Pick a soccer league",leagues,key="league")
        
        if league == "nwsl":
            seasons = ["2024","2023","2022","2021","2020","2019","2018","2017","2016"]
        if league == "mls":
            seasons = ["2024","2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013"]
        if league == "uslc":
            seasons = ["2024","2023","2022","2021","2020","2019","2018","2017"]
        if league == "usl1":
            seasons = ["2024","2023","2022","2021","2020","2019"]
        if league == "mlsnp":
            seasons = ["2024","2023","2022"]
        season = st.selectbox("select season",seasons,key="season")
    bygame = st.checkbox("Group results by game",value=False,key="bygame")
#st.write(st.session_state)
#seasons = ["2023","2024"]
#st.write(season,league,bygame)
@st.cache_data
def loadData(season,league,bygame):
    asa_client = AmericanSoccerAnalysis()
    if bygame == True:
        players_xG = asa_client.get_player_xgoals(leagues=league,season_name=str(season),split_by_games=True)
        players = asa_client.get_players(leagues=league)
        players_gAdded = asa_client.get_player_goals_added(leagues=league,season_name=str(season),split_by_games=True)
        players_gAdded_r = asa_client.get_player_goals_added(leagues=league,season_name=str(season),above_replacement=True,split_by_games=True)
        players_xPass = asa_client.get_player_xpass(leagues=league,season_name=str(season),split_by_games=True)
        teams = asa_client.get_teams(leagues=league)
        games = asa_client.get_games(leagues=league,seasons=str(season))

        games.insert(loc=4,column="Home_Team",value="")
        games.insert(loc=5,column="Away_Team",value="")
        for i,r in games.iterrows():
            for j,rr in teams.iterrows():
                if (r['home_team_id']==rr["team_id"]):
                    games.at[i,'Home_Team'] = rr["team_name"]
                if (r['away_team_id'] == rr["team_id"]):
                    games.at[i,"Away_Team"] = rr["team_name"]
        df5 = players.drop(columns=['season_name'])
        df5 = pd.merge(df5,players_xG,how="inner",on="player_id")
        df5 = df5.drop(columns=['general_position','minutes_played'])
        df5 = df5.merge(players_xPass, on=['player_id', 'game_id','team_id'])
        df5 = df5.drop(columns=['general_position','minutes_played'])
        df5 = df5.merge(players_gAdded, on=['player_id', 'game_id','team_id'])
        df5 = df5.drop(columns=['general_position','minutes_played'])
        df5 = df5.merge(players_gAdded_r, on=['player_id', 'game_id','team_id'])

        
        df5.insert(loc=4,column='team_name',value="")
        for i,r in df5.iterrows():
            for j,rr in teams.iterrows():
                if (r['team_id']==rr['team_id']):
                    df5.at[i,'team_name'] = rr['team_name']
        players_by_game = pd.merge(df5,games,how="inner",on="game_id")
        players_by_game = players_by_game.drop(columns=['player_id','primary_broad_position','secondary_broad_position','secondary_general_position','weight_lb','competition','team_id','game_id','home_team_id','away_team_id','referee_id','stadium_id','home_manager_id','away_manager_id','height_ft','height_in'])

        # Create the desired columns structure
        action_types = ['Dribbling', 'Fouling', 'Interrupting', 'Passing', 'Receiving', 'Shooting']
        keys = ['goals_added_raw', 'goals_added_above_avg', 'count_actions']
        for action in action_types:
            for key in keys:
                column_name = f"{action}_{key}"
                players_by_game[column_name] = players_by_game['data'].apply(lambda x: get_value_from_data(x, action, key))
        result = players_by_game.drop(columns=['data'])
    
    if bygame == False:
        players_xG = asa_client.get_player_xgoals(leagues=league,season_name=str(season),split_by_teams=True)
        players = asa_client.get_players(leagues=league)
        players_gAdded = asa_client.get_player_goals_added(leagues=league,season_name=str(season),split_by_teams=True)
        players_gAdded_r = asa_client.get_player_goals_added(leagues=league,season_name=str(season),split_by_teams=True,above_replacement=True)
        players_xPass = asa_client.get_player_xpass(leagues=league,season_name=str(season),split_by_teams=True)
        teams1 = asa_client.get_teams(leagues=league)
        df1 = players.drop(columns=['season_name'])
        df1 = pd.merge(df1,players_xG,how="inner",on=["player_id"])

        
        df1.insert(loc=4,column='team_name',value="")
        for i,k in df1.iterrows():
            for j,kk in teams1.iterrows():
                if (k['team_id']==kk['team_id']):
                    df1.at[i,'team_name'] = kk['team_name']

        df1 = df1.drop(columns=['general_position','minutes_played'])
        df1 = pd.merge(df1,players_xPass,how="inner",on=["player_id","team_id"])
        df1 = df1.drop(columns=['general_position','minutes_played'])
        df1 = pd.merge(df1,players_gAdded,how='inner',on=["player_id","team_id"])        
        df1 = df1.drop(columns=['general_position','minutes_played'])
        df1 = df1.merge(players_gAdded_r, on=["player_id","team_id"])

        # Create the desired columns structure
        action_types = ['Dribbling', 'Fouling', 'Interrupting', 'Passing', 'Receiving', 'Shooting']
        keys = ['goals_added_raw', 'goals_added_above_avg', 'count_actions']
        for action in action_types:
            for key in keys:
                column_name = f"{action}_{key}"
                df1[column_name] = df1['data'].apply(lambda x: get_value_from_data(x, action, key))
        result = df1.drop(columns=['data'])

    return result

    
if bygame == True:
    #Players_by_game = loadData(st.session_state.season,st.session_state.league,st.session_state.bygame)
    Players_by_game = loadData(season,league,bygame)
    Players = None
    #st.write("by game checked!")
if bygame == False:
    Players_by_game = None
    #st.write("by game not checked!")
    #Players = loadData(st.session_state.season,st.session_state.league,st.session_state.bygame)
    Players = loadData(season,league,bygame)


if bygame == True:
    st.title(league.upper())
    st.header(season)
    st.subheader("Player stats by game")
    st.dataframe(Players_by_game)

    names = Players_by_game['player_name'].unique().tolist()
    if league == "mls":
        name = st.selectbox('Select Player',names,names.index("Lionel Messi"))
    else:
        name = st.selectbox('Select Player',names)
    Players_by_game['goals_added_above_avg'] = Players_by_game['Dribbling_goals_added_above_avg']+Players_by_game['Fouling_goals_added_above_avg']+Players_by_game['Interrupting_goals_added_above_avg']+Players_by_game['Passing_goals_added_above_avg']+Players_by_game['Receiving_goals_added_above_avg']+Players_by_game['Shooting_goals_added_above_avg']
    Players_by_game["Dribbling Factor"] = Players_by_game["Dribbling_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100
    Players_by_game["Shooting Factor"] = Players_by_game["Shooting_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100
    Players_by_game["Passing Factor"] = Players_by_game["Passing_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100
    Players_by_game["Receiving Factor"] = Players_by_game["Receiving_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100
    Players_by_game["Interrupting Factor"] = Players_by_game["Interrupting_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100
    Players_by_game["Fouling Factor"] = Players_by_game["Fouling_goals_added_raw"]/(np.abs(Players_by_game['Dribbling_goals_added_raw'])+np.abs(Players_by_game['Fouling_goals_added_raw'])+np.abs(Players_by_game['Interrupting_goals_added_raw'])+np.abs(Players_by_game['Passing_goals_added_raw'])+np.abs(Players_by_game['Receiving_goals_added_raw'])+np.abs(Players_by_game['Shooting_goals_added_raw']))*100

    selected_player = Players_by_game.loc[Players_by_game['player_name'] == name]
    variable_x = st.selectbox("$$X$$",Players_by_game.columns.to_list(),31)
    variable_y = st.selectbox("$$Y$$",Players_by_game.columns.to_list(),28)

    chart = alt.Chart(selected_player).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('Away_Team',legend=None),
            tooltip=['player_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=500).interactive()
    line = alt.Chart(selected_player).mark_line().encode(x=variable_x,y=variable_y,color=alt.Color('player_name',legend=None))
    st.write(name, " by game")
    st.altair_chart(chart + line, theme="streamlit", use_container_width=True)

    selected_team = selected_player["team_name"].unique().tolist()[0]
    Team = Players_by_game.loc[Players_by_game["team_name"] == selected_team]
    st.header("Team Comparison")
    Teamchart = alt.Chart(Team).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('primary_general_position'),
            tooltip=['player_name','team_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()

    st.altair_chart(Teamchart + line, theme="streamlit", use_container_width=True)
    #OneKnoxPlayers = Players_by_game.loc[Players_by_game['team_name'] == "One Knoxville SC"]
    #'GK', 'CB', 'FB', 'DM', 'CM', 'AM', 'W', and 'ST'.
    #FullBacks = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "FB"]
    #CenterBacks = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "CB"]
    #DMids = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "DM"]
    #CMids = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "CM"]
    #AMids = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "AM"]
    #Wingers = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "W"]
    #Strikers = OneKnoxPlayers.loc[OneKnoxPlayers['primary_general_position'] == "ST"]
    FullBacks = Players_by_game.loc[Players_by_game['primary_general_position'] == "FB"]
    CenterBacks = Players_by_game.loc[Players_by_game['primary_general_position'] == "CB"]
    DMids = Players_by_game.loc[Players_by_game['primary_general_position'] == "DM"]
    CMids = Players_by_game.loc[Players_by_game['primary_general_position'] == "CM"]
    AMids = Players_by_game.loc[Players_by_game['primary_general_position'] == "AM"]
    Wingers = Players_by_game.loc[Players_by_game['primary_general_position'] == "W"]
    Strikers = Players_by_game.loc[Players_by_game['primary_general_position'] == "ST"]

    st.header("Full Backs")
    FBchart = alt.Chart(FullBacks).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('team_name',legend=None),
            tooltip=['player_name','team_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()

    st.altair_chart(FBchart, theme="streamlit", use_container_width=True)

    st.header("Center Backs")
    CBchart = alt.Chart(CenterBacks).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('team_name',legend=None),
            tooltip=['player_name','team_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(CBchart, theme="streamlit", use_container_width=True)

    st.header("Defensive Mids")
    DMchart = alt.Chart(DMids).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('team_name',legend=None),
            tooltip=['player_name','team_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(DMchart, theme="streamlit", use_container_width=True)

    st.header("Center Mids")
    CMchart = alt.Chart(CMids).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('player_name',legend=None),
            tooltip=['player_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(CMchart, theme="streamlit", use_container_width=True)

    st.header("Attacking Mids")
    AMchart = alt.Chart(AMids).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('player_name',legend=None),
            tooltip=['player_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(AMchart, theme="streamlit", use_container_width=True)

    st.header("Wingers")
    Wchart = alt.Chart(Wingers).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('player_name',legend=None),
            tooltip=['player_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(Wchart, theme="streamlit", use_container_width=True)

    st.header("Strikers")
    STchart = alt.Chart(Strikers).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size('goals_added_raw',legend=None),
            color=alt.Color('player_name',legend=None),
            tooltip=['player_name','minutes_played','date_time_utc','Home_Team','home_score','Away_Team','away_score','goals','primary_assists','key_passes','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    st.altair_chart(STchart, theme="streamlit", use_container_width=True)



if bygame == False:
    st.title(league.upper())
    st.header(season)
    Players = Players.loc[Players['minutes_played'] > 0]
    with st.expander("Season Stats - Cumulative"):
        st.dataframe(Players)
    with st.sidebar:
        min_minutes = st.number_input("Minimum Minutes Played",0,10000,300)
    #CALCULATING STATISTICS PER 90
    
    cols=['shots','shots_on_target','goals','xgoals','xplace','key_passes','primary_assists','xassists','xgoals_plus_xassists','points_added','xpoints_added','attempted_passes','passes_completed_over_expected',
        'Dribbling_goals_added_raw','Dribbling_goals_added_above_avg','Dribbling_count_actions','Fouling_goals_added_raw','Fouling_goals_added_above_avg','Fouling_count_actions',
        'Interrupting_goals_added_raw','Interrupting_goals_added_above_avg','Interrupting_count_actions','Passing_goals_added_raw','Passing_goals_added_above_avg','Passing_count_actions',
        'Receiving_goals_added_raw','Receiving_goals_added_above_avg','Receiving_count_actions','Shooting_goals_added_raw','Shooting_goals_added_above_avg','Shooting_count_actions','goals_added_above_replacement']

    summary_per_90 = pd.DataFrame()
    summary_per_90["player_name"] = Players["player_name"]
    summary_per_90["birth_date"] = Players["birth_date"]
    summary_per_90['Club Team'] = Players['team_name']
    summary_per_90['nationality'] = Players['nationality']
    summary_per_90['position'] = Players['general_position']
    summary_per_90['minutes_played'] = Players['minutes_played']
    #summary_per_90['on_Free_Agent_list'] = Players['Free Agent']
    for column in cols:
        summary_per_90[column + "_per90"] = Players.apply(lambda x: x[column]*90/x["minutes_played"], axis = 1)
    summary_per_90['passes_completed_over_expected_p100passes'] = Players['passes_completed_over_expected_p100']
    summary_per_90['goals_added_raw_per90'] = summary_per_90['Dribbling_goals_added_raw_per90']+summary_per_90['Fouling_goals_added_raw_per90']+summary_per_90['Interrupting_goals_added_raw_per90']+summary_per_90['Passing_goals_added_raw_per90']+summary_per_90['Receiving_goals_added_raw_per90']+summary_per_90['Shooting_goals_added_raw_per90']
    summary_per_90['goals_added_above_avg_per90'] = summary_per_90['Dribbling_goals_added_above_avg_per90']+summary_per_90['Fouling_goals_added_above_avg_per90']+summary_per_90['Interrupting_goals_added_above_avg_per90']+summary_per_90['Passing_goals_added_above_avg_per90']+summary_per_90['Receiving_goals_added_above_avg_per90']+summary_per_90['Shooting_goals_added_above_avg_per90']
    summary_per_90["D+I"] = (summary_per_90["Dribbling_goals_added_raw_per90"] + summary_per_90["Interrupting_goals_added_raw_per90"])
    summary_per_90["P+S+F"] = (summary_per_90["Passing_goals_added_raw_per90"]+summary_per_90["Shooting_goals_added_raw_per90"]+summary_per_90["Fouling_goals_added_raw_per90"])
    summary_per_90["Dribbling Factor"] = summary_per_90["Dribbling_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90["Shooting Factor"] = summary_per_90["Shooting_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90["Passing Factor"] = summary_per_90["Passing_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90["Receiving Factor"] = summary_per_90["Receiving_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90["Interrupting Factor"] = summary_per_90["Interrupting_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90["Fouling Factor"] = summary_per_90["Fouling_goals_added_raw_per90"]/(np.abs(summary_per_90['Dribbling_goals_added_raw_per90'])+np.abs(summary_per_90['Fouling_goals_added_raw_per90'])+np.abs(summary_per_90['Interrupting_goals_added_raw_per90'])+np.abs(summary_per_90['Passing_goals_added_raw_per90'])+np.abs(summary_per_90['Receiving_goals_added_raw_per90'])+np.abs(summary_per_90['Shooting_goals_added_raw_per90']))*100
    summary_per_90 = summary_per_90.loc[summary_per_90["minutes_played"] > min_minutes]
    summary_per_90 = summary_per_90.set_index('player_name',drop=False)
    

    mycol = summary_per_90.columns.tolist()


    with st.sidebar:
        selected = st.multiselect('Select Columns',mycol,['birth_date','nationality','Club Team','position','minutes_played'])

    with st.expander("Season Stats - Per 90 Mins"):
        st.dataframe(summary_per_90.loc[:,selected],use_container_width=True)

    
    chart1 = alt.Chart(summary_per_90).mark_circle().encode(
        x='xassists_per90',
        y='xgoals_per90', 
        size=alt.Size('xgoals_plus_xassists_per90',legend=None),
        color=alt.Color('position'),
        tooltip=['player_name','position','Club Team','minutes_played','xgoals_plus_xassists_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()


    '''
    ## Expected Goals vs Expetced Assists
    '''

    st.altair_chart(chart1, theme="streamlit", use_container_width=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Goals added raw vs Goals added above average","Shooting vs Receiving","Passing vs Interrupting","Fouling vs Dribbling"])

    with tab2:
        chart2 = alt.Chart(summary_per_90).mark_circle().encode(
            x='Receiving_goals_added_above_avg_per90',
            y='Shooting_goals_added_above_avg_per90', 
            size=alt.Size('goals_added_above_replacement_per90',legend=None),
            color=alt.Color('position'),
            tooltip=['player_name','position','Club Team','minutes_played','goals_added_above_avg_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()


        '''
        ## Goals Added: Shooting vs Receiving 
        '''
        st.altair_chart(chart2, theme="streamlit", use_container_width=True)

    with tab3:
        chart3 = alt.Chart(summary_per_90).mark_circle().encode(
            x='Interrupting_goals_added_above_avg_per90',
            y='Passing_goals_added_above_avg_per90', 
            size=alt.Size('goals_added_above_replacement_per90',legend=None),
            color=alt.Color('position'),
            tooltip=['player_name','position','Club Team','minutes_played','goals_added_above_avg_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()


        '''
        ## Goals Added: Passing vs Interrupting 
        '''
        st.altair_chart(chart3, theme="streamlit", use_container_width=True)

    with tab4:
        chart4 = alt.Chart(summary_per_90).mark_circle().encode(
            x='Dribbling_goals_added_above_avg_per90',
            y='Fouling_goals_added_above_avg_per90', 
            size=alt.Size('goals_added_above_replacement_per90',legend=None),
            color=alt.Color('position'),
            tooltip=['player_name','position','Club Team','minutes_played','goals_added_above_avg_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()


        '''
        ## Goals Added: Fouling vs Dribbling 
        '''
        st.altair_chart(chart4, theme="streamlit", use_container_width=True)
    
    with tab1:
        chart5 = alt.Chart(summary_per_90).mark_circle().encode(
            x='goals_added_above_avg_per90',
            y='goals_added_raw_per90', 
            size=alt.Size('goals_added_above_replacement_per90',legend=None),
            color=alt.Color('position'),
            tooltip=['player_name','position','Club Team','minutes_played','goals_added_above_avg_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        

        '''
        ## Goals Added: Raw vs Above Avg 
        '''
        st.altair_chart(chart5, theme="streamlit", use_container_width=True)
    st.latex(r'''
        Y = mX + b
        ''')
    variable_x = st.selectbox("$$X$$ ",summary_per_90.columns.to_list(),6)
    variable_y = st.selectbox("$$Y$$",summary_per_90.columns.to_list(),40)
    #Circle_size = st.selectbox("size of circle",summary_per_90.columns.to_list(),5)
    Circle_size = "goals_added_above_replacement_per90"

    chart = alt.Chart(summary_per_90).mark_circle().encode(
            x=variable_x,
            y=variable_y, 
            size=alt.Size(Circle_size,legend=None),
            color=alt.Color('position'),
            tooltip=['player_name','position','Club Team','minutes_played','goals_added_above_avg_per90','goals_per90','primary_assists_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
    line = chart.transform_regression(variable_x,variable_y).mark_line().encode(color=alt.Color(legend=None))
    st.altair_chart(chart + line, theme="streamlit", use_container_width=True)
    st.title("Investigate vs By Position")

    #'GK', 'CB', 'FB', 'DM', 'CM', 'AM', 'W', and 'ST'.
    
    FullBacks = summary_per_90.loc[summary_per_90['position'] == "FB"]
    CenterBacks = summary_per_90.loc[summary_per_90['position'] == "CB"]
    DMids = summary_per_90.loc[summary_per_90['position'] == "DM"]
    CMids = summary_per_90.loc[summary_per_90['position'] == "CM"]
    AMids = summary_per_90.loc[summary_per_90['position'] == "AM"]
    Wingers = summary_per_90.loc[summary_per_90['position'] == "W"]
    Strikers = summary_per_90.loc[summary_per_90['position'] == "ST"]

    position = st.selectbox("Position to view",["Striker","Winger","Attacking Mid","Center Mid","Defensive Mid","Full Back","Center Back"])

    st.latex(r'''
            Y = mX + b
            ''')

    variable_X = st.selectbox("$$X$$ = Dependent Variable/X-Axis",summary_per_90.columns.to_list(),6)
    variable_Y = st.selectbox("$$Y$$ = Independent Variable Variable/Y-Axis",summary_per_90.columns.to_list(),40)
    #Circle_Size = st.selectbox("Circle Size",summary_per_90.columns.to_list(),5)
    Circle_Size = "goals_added_above_replacement_per90"

    

    if position == "Full Back":
        st.header("Full Backs")

        FBchart = alt.Chart(FullBacks).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = FBchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(FBchart + line, theme="streamlit", use_container_width=True)
        
    if position == "Center Back":
        st.header("Center Backs")
        
        CBchart = alt.Chart(CenterBacks).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = CBchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(CBchart + line, theme="streamlit", use_container_width=True)

    if position == "Defensive Mid":
        st.header("Defensive Mids")
        
        DMchart = alt.Chart(DMids).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        line = DMchart.transform_regression(variable_X,variable_Y).mark_line()
        st.altair_chart(DMchart + line, theme="streamlit", use_container_width=True)

    if position == "Center Mid":
        st.header("Center Mids")
        
        CMchart = alt.Chart(CMids).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = CMchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(CMchart + line, theme="streamlit", use_container_width=True)

    if position == "Attacking Mid":
        st.header("Attacking Mids")
        
        AMchart = alt.Chart(AMids).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = AMchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(AMchart + line, theme="streamlit", use_container_width=True)

    if position == "Winger":
        st.header("Wingers")
        
        Wchart = alt.Chart(Wingers).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = Wchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(Wchart + line, theme="streamlit", use_container_width=True)

    if position == "Striker":
        st.header("Strikers")
        
        STchart = alt.Chart(Strikers).mark_circle().encode(
                x=variable_X,
                y=variable_Y, 
                size=alt.Size(Circle_Size,legend=None),
                color=alt.Color(condition=alt.condition(alt.datum.goals_added_above_avg_per90 < 0.0 ,alt.value('red'),alt.value('blue'))["condition"],legend=None),
                tooltip=['player_name','Club Team','minutes_played','goals_per90','primary_assists_per90','xgoals_per90','xplace_per90','key_passes_per90','Shooting Factor','Receiving Factor','Passing Factor','Dribbling Factor','Interrupting Factor','Fouling Factor']).properties(height=600).interactive()
        
        line = STchart.transform_regression(variable_X,variable_Y).mark_line()
        
        st.altair_chart(STchart + line, theme="streamlit", use_container_width=True)