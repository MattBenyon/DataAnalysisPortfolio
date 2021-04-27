# portfolio

`
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'https://www.2kratings.com/lists/top-100-highest-nba-2k-ratings'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify


import pandas as pd
find = soup.find_all('table')[0]
rby = pd.read_html(str(find))


df = rby[0]

df = df.dropna()

positions = (' PG| SG| SF| PF| C')

df['Player'] = df['Player'].str.split(positions).str[0]


df['Player'][1] = 'Stephen Curry'
df['Player'][43] = 'Clint Capela'
df['Player'][50] = 'John Wall'
df['Player'][54] = 'Mike Conley'
df['Player'][73] = 'Wendell Carter Jr.'
df['Player'][88] = 'Brandon Clarke'
df['Player'][98] = 'Jordan Clarkson'

from nba_api.stats.endpoints import leaguedashplayerstats

playerstats_df = pd.read_csv('latest_RAPTOR_by_player.csv')
# measure_type_detailed_defense="Advanced",
names = df.Player


filtered_df = playerstats_df[playerstats_df['player_name'].isin(names)]
filterednames_df = df[df['Player'].isin(playerstats_df['player_name'])]
filterednames_df = filterednames_df.sort_values('Player')
filtered_df = filtered_df.sort_values('player_name')
import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')




fig, ax = plt.subplots()
plot =ax.scatter(filterednames_df['OVR'],(filtered_df['war_total']),
            marker="o",alpha=0.8, cmap='viridis_r',s=250,c=filtered_df['war_total'])

plt.ylabel('Player Impact Estimate', fontsize=20,labelpad=20)
plt.xlabel('NBA 2K rating', fontsize=20,x=0.48)

plt.rcParams['figure.figsize'] = (12, 11)

ax.text(76,-4,'Source: fivethirtyeight.com, 2kratings.com                                                                Author: Matt Benyon, @matt_benyon',
        fontsize = 16, color = '#f0f0f0', backgroundcolor = 'grey')

ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
ax.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

ax.text(x = 76.5, y = 16, s = "NBA 2K ratings correlate very little with FiveThirtyEights\nRAPTOR WAR metric",
               fontsize = 30, weight = 'bold', alpha = .75)
ax.text(x = 76.5, y = 14.8,
               s = 'Many players in the 82-87 overall range have a higher impact according to RAPTOR WAR.\nRatings correct as of 27/04/21',
              fontsize =20, alpha = .85)
ax.set_xlim(left = 78, right = 99)
x = [80,85,90,95,99]
labels=["80","85","90","95","99"]
plt.xticks(x, labels,fontsize=20)

plt.savefig('2kratings.png',bbox_inches='tight')



plt.show()

`
