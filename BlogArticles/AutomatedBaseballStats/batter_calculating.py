'''
Written by Andrew Holtzman-Marga, owner and chief editor of the blog Connecting the Game
https://connectingthegame.azurewebsites.net
'''

import csv

#define variables 
avg = 0
obp = 0
slg = 0
ops = 0
babip = 0
iso = 0
singles = 0
tb = 0

#each player's stats -- rows
playerStats = []

#opening our data for reference
o = open("batter_partial_data.csv", "r")
myData = csv.reader(o)
for rw in myData:
    #each player's stats are added to an array
    playerStats = rw

    #variables for calculations
    ab = int(playerStats[7])
    h = int(playerStats[9])
    doubles = int(playerStats[10])
    triples = int(playerStats[11])
    hr = int(playerStats[12])
    bb = int(playerStats[16])
    so = int(playerStats[17])
    hbp = int(playerStats[20])
    sf = int(playerStats[22])

    #calculations
    avg = round((h/ab),3)
    obp = round((h+bb+hbp)/(ab+bb+hbp+sf),3)
    
    singles = h-(doubles+triples+hr)
    tb = singles + 2*(doubles) + 3*(triples) + 4*(hr)

    slg = round((tb/ab),3)
    ops = round((obp+slg),3)

    babip = round((h-hr)/(ab-so-hr+sf),3)
    iso = round((slg-avg),3)

    #printing results
    print(playerStats[1])
    print("AVG",avg)
    print("OBP",obp)
    print("SLG",slg)
    print("OPS",ops)
    print("BABIP",babip)
    print("TB",tb)
    print("ISO",iso)
