import pandas as pd
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Basic Stats Parser
URL = 'https://www.basketball-reference.com/players/e/embiijo01/gamelog/2021/'
soup = BeautifulSoup(urlopen(URL), "html.parser")
for elem in soup.findAll("table", {"id": "pgl_basic"}):
    print(str(elem))
data = [{}]

stats = ["game_season", "fg_pct", "fg3_pct", "ft_pct", "orb",
         "drb", "trb", "ast", "stl", "blk", "tov", "pf", "pts", "plus_minus"]

# Find the number of games played
num_games = len(soup.findAll("td", {"data-stat": "game_season"}))

# Get all the stats from the webpage and put them into arrays
for stat in stats:
    curr_stat = num_games * [None]
    i = 0
    for elem in soup.findAll("td", {"data-stat": stat}):
        mystr = str(elem)
        curr_stat[i] = mystr[mystr.find(">") + 1: mystr.find("<", 1)]
        i += 1
    data.append({stat: curr_stat})

# Address the DNPs by adding nothing into the respective indices of the stat arrays, make sure array lengths are the same
data = data[1:]
added_games = []
for i in range(0, len(data[0]["game_season"])):
    if data[0]["game_season"][i] == '':
        added_games.append(i)

# Add in the DNP games
index = 0
name = 1
for i in range(0, len(added_games)):
    name = 1
    for data_pt in data[1:]:
        data_pt[stats[name]].insert(added_games[i], 'N/A')
        name += 1

# Trim the Nones
name = 1
for data_pt in data[1:]:
    new_data_pt = list(filter(None, data_pt[stats[name]]))
    data_pt[stats[name]] = new_data_pt
    name += 1

name = 0
for data_pt in data:
    print(data_pt)
    print()
    name += 1
