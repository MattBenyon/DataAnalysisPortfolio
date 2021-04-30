# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:13:11 2021

@author: mattb
"""

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

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/allstar/NBA_2021_voting-frontcourt-eastern-conference.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify

find = soup.find_all('table')[0]
rby = pd.read_html(str(find))


df1 = rby[0]

url = 'https://www.basketball-reference.com/allstar/NBA_2021_voting-frontcourt-western-conference.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify

find = soup.find_all('table')[0]
rby = pd.read_html(str(find))


df2 = rby[0]

url = 'https://www.basketball-reference.com/allstar/NBA_2021_voting-backcourt-eastern-conference.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify

find = soup.find_all('table')[0]
rby = pd.read_html(str(find))


df3 = rby[0]

url = 'https://www.basketball-reference.com/allstar/NBA_2021_voting-backcourt-western-conference.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.prettify

find = soup.find_all('table')[0]
rby = pd.read_html(str(find))


df4 = rby[0]

df1 = df1.append(df2, ignore_index=True)
df1 = df1.append(df3, ignore_index=True)
df1 = df1.append(df4, ignore_index=True)
df1 = df1.iloc[:, 1:4]
df1.columns = [''] * len(df1.columns)
df1.columns = ['Player','Votes','Rank']

playerstats_df = df1

names = df.iloc[:, 1]



filtered_df = playerstats_df[playerstats_df['Player'].isin(names)]
filterednames_df = df[df['Player'].isin(playerstats_df['Player'])]
filterednames_df = filterednames_df.sort_values('Player')
filtered_df = filtered_df.sort_values('Player')

filtered_df = filtered_df.sort_values("Player")

filtered_df['Rank'] = filtered_df['Votes'].rank(ascending=False)


import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')


fig, ax1 = plt.subplots()
plot =ax1.scatter(filterednames_df['OVR'],(filtered_df['Votes']),
            marker="o",alpha=0.8, cmap='viridis_r',s=250,c=filterednames_df['OVR'])


plt.ylabel('All-star fan votes (logged)', fontsize=20,labelpad=10)
plt.xlabel('NBA 2K rating', fontsize=20,x=0.48,labelpad=10)
ax1.set_yscale('log')
plt.rcParams['figure.figsize'] = (15, 10.5)

ax1.text(76.3,1e3,'Source: basketball-reference.com, 2kratings.com                                                                     Author: Matt Benyon, @matt_benyon',
        fontsize = 16, color = '#f0f0f0', backgroundcolor = 'grey')

ax1.tick_params(axis = 'both', which = 'major', labelsize = 18)
ax1.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

ax1.text(x = 76.5, y = 1.5e7, s = "NBA 2K ratings correlate strongly with All-Star fan voting.\n",
              fontsize = 30, weight = 'bold', alpha = .75)

ax1.text(x = 76.5, y = 9e6,
               s = 'Players with more all-star fan votes are more likely to have a higher NBA 2K rating, which could\nsuggest that the ratings are based on a combination of impact but also popularity.\nRatings correct as of 27/04/21',
              fontsize =20, alpha = .85)

ax1.set_xlim(left = 78, right = 99)

x = [80,85,90,95,99]
labels=["80","85","90","95","99"]
plt.xticks(x, labels,fontsize=20)
x = [1e4,1e5,1e6]
labels=["10k","100k","1m"]
plt.yticks(x, labels,fontsize=20)

from scipy.optimize import curve_fit
import numpy as np

order = np.argsort(filterednames_df['OVR'])
x = np.array(filterednames_df['OVR'], dtype=float)[order] #transform your data in a numpy array of floats 
y = np.array(filtered_df['Votes'], dtype=float)[order] #so the curve_fit can work

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 +c*x + d

popt, pcov = curve_fit(func, x, y)

plt.plot(x, func(x, *popt),c="darkslateblue", lw=3,alpha=0.8,linestyle='--')

plt.savefig('2kvsvotesLOG.png',bbox_inches='tight')

plt.show()

