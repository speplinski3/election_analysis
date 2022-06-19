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

#Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

#Step 1: Create a county list and county votes dictionary.
county_options = []
votes_county = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Step (2) Track the largest county and county voter turnout
county_mostname = ""
county_mostvotes = 0
county_winpercentage = 0

#Read the csv and convert it to a list of dictionaries.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

#Read the header
    header = next(reader)

#For each row in the CSV file.
    for row in reader:
        #Add to the total vote count
        total_votes = total_votes + 1

        #Get the candidate name from each row.
        candidate_name = row[2]

        #Extract the county name from each row.
        county_name = row[1]

        #If the candidate does not match and existing candidate add it to the 
        # candidate list.
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

        #If county does not make any existing county in the list, then add.

        if county_name not in county_options:
            
            county_options.append(county_name)
            
            votes_county[county_name] = 0

        votes_county[county_name] += 1

# #Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote county (to terminal):
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # txt_file.write(election_results)
    #6: Write a for loop to get county from county dictionary. 
    #Retrieve the county vote count.
    #Calculate the percentage of votes for the county.
    for county_name in votes_county:
        countyvotes = votes_county.get(county_name)
        countyvotes_percentage = float(countyvotes) / float(total_votes) * 100  
        county_results = (
            f"{county_name}: {countyvotes_percentage:.1f}% ({countyvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    #Print the county with the largest turnout to the terminal.
        if (countyvotes > county_mostvotes) and (countyvotes_percentage > county_winpercentage):
            county_mostvotes = countyvotes
            county_winpercentage = countyvotes_percentage
            county_mostname = county_name
        county_winner_summary = ( 
            f"------------------------\n"
            f"County Winner: {county_mostname}\n"
            f"------------------------\n")
    print(county_winner_summary)
    txt_file.write(county_winner_summary)
    #8. Save the county with the largest turnout to a text file.

    #Save the final candidate vote count to the text file.

    for candidate_name in candidate_votes:

        #Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print cacndidate voter count and percentage to the terminal.
        print(candidate_results)
        txt_file.write(candidate_results)
        #Save the candidate results to our text file.
                
#Determine winning vote county, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage 
#Print the winning candidate (to terminal)
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
