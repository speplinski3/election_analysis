# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = 'analysis/election_results.csv'
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#Step (1) (a.) Initialize a county list
county_options = []

# (b.) Initialize a dictionary for county as key and votes for each county as values.
votes_county = {}

#Step (2) (a.) Initialize an empty string for county name, largest turnout.
county_mostname = ""
# (b.) Initialize a variable that will hold number of votes of largest county turnout.
county_mostvotes = 0
county_winpercentage = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Step (3) Extract the county name from each row.
        county_name = row[1]

        #Step (4ab) Check if county name is in county list and add if not in list.
    if county_name not in county_options:
        county_options.append(county_name)

        #Step (4c) Initialize county vote to 0.
        votes_county[county_name] = 0

        #Step (5) Add to county's vote while looping through rows.
        votes_county[county_name] += 1

        #Step (6a) Write repition statement to get the county from the county dictionary.
        for county_name in votes_county:
        #Step (6b) Initialize variable to hold county's votes as retrieved from dictionary.
            countyvotes = votes_county.get(county_name)

        #Step (6c) Write a script that calculates the county's votes as a percentage of the total votes.
            countyvotes_percentage = float(countyvotes) / float(total_votes) * 100
            county_results = (
                f"{county_name}: {countyvotes_percentage:.2f}% ({countyvotes:,})\n"
        )
        #Step (6d) Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.
        print(county_results)

        #Step (6e) DELIVERABLE 2

        #Step (6f) Write a decision statement that determines the county with the largest vote count and then adds county and vote count to variables in Step 2.
        if (countyvotes > county_mostvotes) and (countyvotes_percentage > county_winpercentage):
            county_mostvotes = countyvotes
            county_winpercentage = countyvotes_percentage
            county_mostname = county_name

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1




# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
