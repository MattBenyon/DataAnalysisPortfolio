# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:13:11 2021

@author: mattb
"""
# import some required packages
import requests
import urllib.request
from bs4 import BeautifulSoup

#define url as string
#request access to url
url = 'https://www.2kratings.com/lists/top-100-highest-nba-2k-ratings'
response = requests.get(url)


#use beautiful soup and pandas to create a dataframe
soup = BeautifulSoup(response.text, "html.parser")
soup.prettify

import pandas as pd

find = soup.find_all('table')[0]
rby = pd.read_html(str(find))

#select first dataframe avaialable
df = rby[0]

#drop nans
df = df.dropna()

#Splitting player names when their is a space followed by position
#This leaves behind just the player name
positions = (' PG| SG| SF| PF| C')

df['Player'] = df['Player'].str.split(positions).str[0]


#Some player names were incorrect so manually replace
df['Player'][1] = 'Stephen Curry'
df['Player'][43] = 'Clint Capela'
df['Player'][50] = 'John Wall'
df['Player'][54] = 'Mike Conley'
df['Player'][73] = 'Wendell Carter Jr.'
df['Player'][88] = 'Brandon Clarke'
df['Player'][98] = 'Jordan Clarkson'


#next is getting the all-star votes data
#this required 4 seperate dataframes, that were then appended to the bottom of the first dataframe

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

#df1 now contains all all-star votes independent of conference and position

#remove unnecessary columns
df1 = df1.iloc[:, 1:4]

#rename columns
df1.columns = ['Player','Votes','Rank']

#make new dataframe with more applicable name
playerstats_df = df1

#select names and add to list
names = df.iloc[:, 1]


#filter out any players that dont appear in names
filtered_votes_df = playerstats_df[playerstats_df['Player'].isin(names)]
filtered_ratings_df = df[df['Player'].isin(playerstats_df['Player'])]

#sort both data frames to be alphabetical
filtered_ratings_df = filtered_ratings_df.sort_values('Player')
filtered_votes_df = filtered_votes_df.sort_values('Player')


#import matplotlib to plot the results
import matplotlib.pyplot as plt

#use the fivethirtyeight style to achieve a more proffesional appearance
plt.style.use('fivethirtyeight')

#Plot the data and format
fig, ax1 = plt.subplots()
plot =ax1.scatter(filtered_ratings_df['OVR'],(filtered_votes_df['Votes']),
            marker="o",alpha=0.8, cmap='viridis_r',s=250,c=filtered_ratings_df['OVR'])


plt.ylabel('All-star fan votes / million', fontsize=20,labelpad=10)
plt.xlabel('NBA 2K rating', fontsize=20,x=0.48,labelpad=10)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.rcParams['figure.figsize'] = (15, 10.5)

ax1.text(76.3,-1.1e6,'Source: basketball-reference.com, 2kratings.com                                                                     Author: Matt Benyon, @matt_benyon',
        fontsize = 16, color = '#f0f0f0', backgroundcolor = 'grey')

ax1.tick_params(axis = 'both', which = 'major', labelsize = 18)
ax1.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

ax1.text(x = 76.5, y = 6.8e6, s = "NBA 2K ratings correlate strongly with All-Star fan voting.\n",
               fontsize = 30, weight = 'bold', alpha = .75)

ax1.text(x = 76.5, y = 6.45e6,
               s = 'Players with more all-star fan votes are more likely to have a higher NBA 2K rating, which could\nsuggest that the ratings are based on a combination of impact but also popularity.\nRatings correct as of 27/04/21',
              fontsize =20, alpha = .85)
ax1.set_xlim(left = 78, right = 99)
x = [80,85,90,95,99]
labels=["80","85","90","95","99"]
plt.xticks(x, labels,fontsize=20)
x = [1e6,2e6,3e6,4e6,5e6,6e6]
labels=["1","2","3","4","5","6"]
plt.yticks(x, labels,fontsize=20)

#import curve fit to fit a curve to the data

from scipy.optimize import curve_fit
import numpy as np


order = np.argsort(filtered_ratings_df['OVR'])
x = np.array(filtered_ratings_df['OVR'], dtype=float)[order] #transform data in a numpy array of floats 
y = np.array(filtered_votes_df['Votes'], dtype=float)[order] #so the curve_fit can work

def func(x, a, b, c, d):   #use a cubic function to get a good shape
    return a*x**3 + b*x**2 +c*x + d

popt, pcov = curve_fit(func, x, y)

plt.plot(x, func(x, *popt),c="darkslateblue", lw=3,alpha=0.8,linestyle='--')

plt.savefig('2kvsvotes.png',bbox_inches='tight')

plt.show()

