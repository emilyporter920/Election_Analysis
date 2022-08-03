# Election Analysis

## Overview
Performed analysis on the election results for the Colorado state elections.

### Purpose
This analysis was performed using Python to find the following data for the Colorado election commission:

* The total number of votes
* The total number of county votes and their percentage of the total vote
* The largest county turnout based on number of county votes
* The number of votes for each candidate along with the percentage of the total vote
* The number of votes for the winning candidate along with the percentage of the total vote

## Election-Audit Results
All data listed above has been printed into a text file, seen below in **Figure 1.1** for easy access:

1. Total votes cast in this congressional election:

    Total Votes: 369,711

<br/>

2. Number of votes and percentage of the total vote for each county:

    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)

<br/>

3. County that had the largest number of votes:

    Largest County Turnout: Denver

<br/>

4. Number of votes and percentage of the total vote for each candidate:

    Charles Casper Stockham: 23.0% (85,213)

    Diana DeGette: 73.8% (272,892)

    Raymon Anthony Doane: 3.1% (11,606)

<br/>

5. Number of votes and percentage of the total vote for the winning candidate:

    Winner: Diana DeGette

    Winning Vote Count: 272,892

    Winning Percentage: 73.8%

<br/>

<p align="center">
  <img 
    width="500"
    height="500"
    src=Resources/Election_analysis_txt.png
  >
</p>

<div align="center"
<p><b> Figure 1.1 </b></p>
</div>


### Example of Python Code Used for Analysis
Below in **Figure 1.2** is an example of how candidates votes and county votes were added and counted by using if statements. The if statement asks if the county name was found in the list; if not it will be added to the list and each time the county name is found it will add 1 to the total votes for that county.

    # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name]=0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        )

<div align="center"
<p><b> Figure 1.2 </b></p>
</div>

## Election-Audit Summary
* The code written above found in the PyPoll_Challenge.py file can be used for any congressional election to find all of the data listed above.
* This script can be modified to show both state and local level election results by changing the file loaded to the desired data.

## Questions

* You can contact me via email or GitHub!

    * Email: emilyporter920@gmail.com
    * GitHub Profile: Emily Porter || github.com/emilyporter920 
