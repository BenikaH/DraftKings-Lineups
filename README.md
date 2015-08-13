# **DraftKings_Lineups**

##**Summary**
The purpose of this program is to quickly and easily compare your player choices to those made by the other players (or group of players) in the tournament.  This is done by importing the Draft Kings lineup history, which is a CSV file provided by DK that shows each entry to the tournament, their score and the team they selected.  The program can use this information to generate some general tournament info and a breakdown of the highest owned players at each position, represented by bar charts.  

##**Why Use?**
It is hard to determine your true skill by relying on your past results. Because of the variance in DFS it is possible that a true winner is in the red or that a true loser is turning a profit. In the long term, your true colors will show and will have a better picture if you are actually a winning or losing player, but it could be an expensive study to actually get to the long term if you are intrinsically a losing player.  Therefore, the best strategy to actually determine if you’re putting together quality teams, is to be in line with the same thought process of some of the games proven winners.  

##**How To Use **
1.  Set up the database by editing the db.ini file with your database credentials
2.  You’re going to need the CSV files to see results. Go to one of your contest histories and download the file via the link under the standings window. After downloading, add these files to the ‘in_files’ folder in your project directory to be read by the program.
3.  Start the program by running game_history.py.  If not set, it will prompt you for your username.  If available CSV files are in the ‘in_foler’ it will open the window to add them automatically, else open ‘Edit Tourney Info’ from the Settings menu.  
4.  Open the ‘Add to Following’ window from the Settings menu to add players to compare your players to.  
5.  Restart program to refresh newly added settings/tournament data.  Auto updating after a change is a work in progress.  

##**Requirements**
Python 2.6
PyQt4
MySQLdb
matplotlib

##**Notes**
- Only download a CSV file from Draft Kings after the tournament has completed. You can download them while the tournament is running, but he file is in a different format and will not work.  
- There are 2 rows of charts generated: the top row will be calculated from *all* of the entries in the tournament, while the bottom row will just be the selected usernames added in step 4 (if entries are present).  
- As a general rule of thumb, you want highly correlated ownership in cash games but often the opposite in GPPs. Because of this, this program will be more useful in cash games.  
- This is just a rough draft and definitely needs a few things ironed out/added.
  
