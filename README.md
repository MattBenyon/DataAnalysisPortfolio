# [Matt Benyon](https://github.com/MattBenyon?tab=repositories)

This page is a summary of some projects that I have undertaken to demonstrate by ability as a data analyst and data scientist. I hope you take the time to read through the summaries/write-ups and/or view my code avaialable in the GitHub repository.

# 1. [NBA 2K player ratings analysis](https://github.com/MattBenyon/2K-Ratings)
- Acquiring the data: Scraped data from [2kratings.com](https://www.2kratings.com/), [basketballreference.com](https://www.basketball-reference.com/allstar/NBA_2021_voting.html)            and downloaded .csv file from [FiveThirtyEight](https://projects.fivethirtyeight.com/nba-player-ratings/). 
- Cleaning the data: Cleaned the data by renaming columns, dropping nan's, splitting strings so player names matched format across dataframes etc.
- Plotting the data: Used MatPlotLib to create plots of All-Star votes against NBA 2K ratings, FiveThirtyEights RAPTOR WAR metric against 2K ratings among others. Used Scipy package to fit a line to the appropriate figures. Provided a logarithmic version to show correlation.
- Project was completed at own leisure as a test of my developing scraping, cleaning and analysing skills. I wanted to test a hypothesis I had that NBA 2K player ratings were swayed more by popularity than by defensive impact. I verified this hypothesis but also acknowldged that a players popularity is mostly a product of their offensive ability. Overall I found that defensive impact had little correlation with a players rating and player popularity correlated strongly.

An example figure from the study:

![2K rating vs All-star votes](https://raw.githubusercontent.com/MattBenyon/2K-Ratings/main/figures/2kvsvotesLOG.png "NBA all-star votes plotted on a log scale against NBA 2K rating")

Feel free to check out my write up available at the hyperlink on the heading or through my GitHub page.
> Write-up coming soon once completed undergraduate exams

# 2. [Linear Regression of the basketball 'four factors' from previous seasons to predict a teams success in the current season, based on the same metrics](https://mattbenyon.github.io/FourFactorsLinearRegression/)
> Project completed but need to write up and summarise my findings, will complete after undergraduate exams


`print('hello world')`


# 3. [Analysis of Warzone loadout META I complete to determine which weapon choices are effective but underutilised](https://github.com/MattBenyon/WarzoneMETA)

![Warzone meta](https://raw.githubusercontent.com/MattBenyon/WarzoneMETA/main/WarzoneMeta.png)

"Meta can be used as an acronym for 'most effective tactics available' and calling something 'meta' means that it’s an effective way to achieve the goal of the game, whether it’s to beat other players or beat the game itself" according to https://www.grammarly.com/blog/meta-meaning/

I was attemtpting to recreate this style from the patch notes of a different game 
![Rainbow Six Siege Example](https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6LdEzBUjina2GF5jVEyjtv/bc61617cdf26ec488bbdb42b1156ff67/BalancingMatrixAtt_Y6S13.png)
