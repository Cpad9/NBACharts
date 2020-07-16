from pandas import *
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs
from datetime import date
from datetime import timedelta

import numpy as np


    ##Time Stuff
today = date.today()
dateString = today.strftime("%Y-%m-%d")
oneWeek = (today - timedelta(7)).strftime("%Y-%m-%d")
oneYear = (today - timedelta(365)).strftime("%Y-%m-%d")

    ##Get Stephen Curry Game Logs
# df = get_game_logs('Stephen Curry', oneYear, dateString) 
# print(df)


    ##Write to HTML
# text_file = open("table.html", "w")
# text_file.write(html.render())
# text_file.write(df.to_html())
# text_file.close()

    ##Create Loop to go through teams
teamsText = open("teamNames.txt",'r')

####Seperate Team Abbreviation and Team Name, Make List of Team Abrvs
allTeamAbrv = []
for line in teamsText:
    teamAbrv = line.split(':')[1]
    teamName = line.split(':')[0]
    # print(teamName)
    # print(teamAbrv)
    #teamAbrv[] for abbreviation, Can use .strip()
    teamAbrv = teamAbrv[1:4]
    allTeamAbrv.append(teamAbrv)

print(allTeamAbrv)
teamsText.close()


    ##Get Players from allteamAbbrvs##
#Create List
allPlayers = []
for team in allTeamAbrv:
    print(f'\n{team}\n')
        #Get Each team's Roster
    theRoster = get_roster(team, 2019)
    # print(theRoster)
    # print(theRoster['PLAYER'])
        #Grab only 'PLAYER' info from Dataframe -> Create a List from Dataframe
    justPlayerName = theRoster['PLAYER'].values.tolist()
        #We use '.extend' so it adds each player to the list
    allPlayers.extend(justPlayerName)
        #If we used
    # allPlayers.append(justPlayerName)
        # allPlayers would look like [['Jaylen Adams', 'Justin Anderson']['Aron Baynes','Jaylen Brown']]
        # Instead of looking like
        #                            ['Jaylen Adams', 'Justin Anderson','Aron Baynes','Jaylen Brown']

    ##Write Players to .txt File##
# players_file = open("AllPlayers.txt","a")
# allPlayersString = '\n'.join(allPlayers)
# players_file.write(allPlayersString)
# players_file.close()
    
print('\n\nGetting Game Logs\n\n')
    #Get_game_logs for each player and Save into .csv file
players = iter(allPlayers)

for player in players:
    #Maybe dont need
    if player is None:
        next(players)
    print(f'\n\n{player} logs \n')
    spacesRemoved = player.replace(" ","") 
    if spacesRemoved.isalpha() == False:
        next(players)
    else:
        gameLogs = get_game_logs(player, oneYear, dateString) 
        #Save gamelogs to .csv
        if gameLogs is None:
            next(players)
        else:
            gameLogs.to_csv(f'PlayerGameLogs/{player}.csv', index=False)
            print(gameLogs)

 







###########################################################################
###################WORK IN PROGRESS ########################################

#######Trying to figure out how to save a dataframe to SQL
# https://www.dataquest.io/blog/sql-insert-tutorial/

#     #One Player in Game logs
# gameLog = get_game_logs('Stephen Curry', oneYear, dateString)
# print(gameLog)

# import pymysql

# # Connect to Database
# connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='12345',
#                             db='gamelog')

# #Create Cursor (Allows us to execute SQL queries)
# cursor=connection.cursor()

    





