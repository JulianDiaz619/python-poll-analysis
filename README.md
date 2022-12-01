# Python Poll Analysis
## Overview of Election Audit
The purpose of this analysis was to find the total votes, the largest county turnout, the winner of the election, and percentages including voters for every candidate, as well as the total amount of votes per candidate.
## Election Audit Results
This section will be going over:
* Total Votes
* Largest County Turnout
* Percentages of voters for each candidate
* Winner of the election
The final results will be shown at the end of the README.
#### Total Votes
![image](/resources/total_votes.png)
![image](/resources/total_votes_code.png)

  To calculate the total number of votes, Shown above is a variable set to zero to increment in a loop. The second image is the code that skips the header, and loops through every row adding a vote to our total_votes_counties variable after every iteration until it has gone through all of the rows.

#### Largest County Turnout
![image](/resources/CountyTurnout.png)

  The code above shows a for loop that gathers the percentages for each county and prints them all out accordingly. Below that is an if statement to figure out which county had the largest turnout and to print that out. Everything is then saved to the text file.

## Election Audit Summary

