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

#### Percentage of Voters and Election Winner
![image](/resources/electionwinner.png)

  The code above is quite similar to the code used for the county voter percentages as well as the largest voter turnout, except its to calculate the voter percentages for each candidate rather than county, and to find the winner of the election. It begins with a for loop that gathers and prints according percentages to whomever candidate it is currently on. After there is an if statement that find the candidate with the most amount of votes deeming them the winner. The main difference between this code and the one seen in "Largest County Turnout" is simply the fact that there is more in the printed statement at the end. This one has the winner of the election as well as their total votes and voter percentage.

#### General Results
 ![image](/resources/terminal.png)
  
 Shown above is what prints in the VSCode terminal. As you can see, Denver has a significant amount more voters than Jefferson and Arapahoe do. Written below those results you can see the percentages for the candidates, showing that Diana also has a significant more amount of voters. Next to the percentages you can see the total amount of votes the county or candidate has accumulated. The winner is shown at the end showing their name as well as their voter count and voter percentage. 
 
## Election Audit Summary
  
  This code can be used for any election. The only things that would have to be taken into account is that another dataset may look differently, and the candidates/counties may be on different indexes meaning we would have to modify which index is set to county. We would also have to modify the index that are set to candidate accordingly. Seen below are the current indexes the county and candidate fall on in this dataset.

![image](/resources/countyindex.png)
![image](/resources/candidateindex.png)
  
