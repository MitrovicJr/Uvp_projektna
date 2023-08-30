# Uvp_projektna

The porgam uses the official nba website to analyse statistics of players for the 2022-2023 season.
The information on the wensite is quite extensive, and the program is just a bare bones analysis which can be scaled easily using weighted projections and introducing more variables to filter the players. 
It takes an input of an nba player that must be on the list and retrieves his total points, assists and rebounds as well as his team and minutes played for the 2022-2023 season. 
It then compares the player to others players on the list and lists 3 more players that exhibit the most similar stats to the listed player using a very simple distance calculation. The parameters are not weighed so some stats are much more prevalent.
Afterwards it stores the main statistical data of the players and plots a graph of points to minutes played, as well as a simple regression line.
I have always made sure that the name of player input can be capitalised in any way the user deems fit. 
(I am sure there are much more effective ways than this code to achieve this task, it is just what I found to be most intuitive for a beginner like me)
