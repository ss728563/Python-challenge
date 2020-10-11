# Create a Python script that analyzes the votes and calculates each of the following:
#  Total number of votes cast
#  A complete list of candidates who received votes
#  The percentage of votes each candidate won
#  The total number of votes each candidate won
#  The winner of the election based on popular vote


# Import modules. os for path, csv for file
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# create a path to read CSV file
election_data = os.path.join("..","Resources", "/Users/salitasantiago/python-challenge/PyPoll/Resources/election_data.csv")
# Open & read csv file
with open(election_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)

    # Read the header row first
    csv_header = next(csv_reader)

    # Loop each row of data after the header
    for row in csv_reader:

        voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    # Count votes per candidate in most common outcome order & append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # Calculate the percentage of votes per candidate by 3 decimals
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    
# Print analysis to terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("------------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("------------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("------------------------------")


# Export text file with results
election_file = os.path.join("Output", "/Users/salitasantiago/python-challenge/PyPoll/Analysis/election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")   