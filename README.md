# NOTE

# *Dear reader*,
this page is outdated and mainly composes of work from outside my studies. Since I have been compelting a masters degree in data science, I have had little time to update this page with some of my newer/better work. Feel free to look, but if you would like to see more evidence of proficiency, please do get in touch: mattbenyon@hotmail.com


# [Matt Benyon](https://github.com/MattBenyon?tab=repositories)

This page is a summary of some projects that I have undertaken to demonstrate by ability as a data analyst and data scientist. I hope you take the time to read through the summaries/write-ups and/or view my code avaialable in the GitHub repository.


# 1. [Basketball four factors analysis](https://github.com/MattBenyon/FourFactorsRegression/tree/master)
Linear Regression of the basketball 'four factors' from previous seasons to predict a teams win totals in the current season.
> Project completed, write-up is in progress



# 2. [NBA 2K player ratings analysis](https://github.com/MattBenyon/2K-Ratings)
- Acquiring the data: Scraped data from [2kratings.com](https://www.2kratings.com/), [basketballreference.com](https://www.basketball-reference.com/allstar/NBA_2021_voting.html)            and downloaded .csv file from [FiveThirtyEight](https://projects.fivethirtyeight.com/nba-player-ratings/). 
- Cleaning the data: Cleaned the data by renaming columns, dropping nan's, splitting strings so player names matched format across dataframes etc.
- Plotting the data: Used MatPlotLib to create plots of All-Star votes against NBA 2K ratings, FiveThirtyEights RAPTOR WAR metric against 2K ratings among others. Used Scipy package to fit a line to the appropriate figures. Provided a logarithmic version to show correlation.
- Project was completed at own leisure as a test of my developing scraping, cleaning and analysing skills. I wanted to test a hypothesis I had that NBA 2K player ratings were swayed more by popularity than by defensive impact. I verified this hypothesis but also acknowldged that a players popularity is mostly a product of their offensive ability. Overall I found that defensive impact had little correlation with a players rating and player popularity correlated strongly.

An example figure from the study:

![2K rating vs All-star votes](https://raw.githubusercontent.com/MattBenyon/2K-Ratings/main/figures/2kvsvotesLOG.png "NBA all-star votes plotted on a log scale against NBA 2K rating")

Feel free to check out my write up available at the hyperlink on the heading or through my GitHub page.
> Write-up coming soon once completed undergraduate exams




