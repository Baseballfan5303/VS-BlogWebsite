'''
Written by Andrew Holtzman-Marga, owner and chief editor of the blog Connecting the Game
https://connectingthegame.azurewebsites.net
'''

import csv

#define variables 
era = 0
erap = 0
whip = 0
fip = 0
lg_era = 4.49
fip_const = 3.1

#each player's stats -- rows
playerStats = []

#opening our data for reference
o = open("pitcher_partial_data.csv", "r")
myData = csv.reader(o)
for rw in myData:
    #each player's stats are added to an array
    playerStats = rw

    #variables for calculations
    ip = float(playerStats[14])
    h = int(playerStats[15])
    er = int(playerStats[17])
    hr = int(playerStats[18])
    bb = int(playerStats[19])
    k = int(playerStats[21])
    hbp = int(playerStats[22])

    #calculations
    era = round( ((9*er)/ip) ,2)
    erap = round( (100*(lg_era/era)) ,2)
    whip = round( ((bb+h)/ip) ,2)
    fip = round( (((13*hr)+(3*(bb+hbp))-(2*k))/ip)+fip_const ,2)

    #printing results
    print(playerStats[1])
    print("ERA",era)
    print("ERA+",erap)
    print("WHIP",whip)
    print("FIP",fip)
