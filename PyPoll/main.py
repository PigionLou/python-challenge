
#importing dependencies
import os
import csv

#assiging path
csvpath = os.path.join('Resources','election_data.csv')

votecounter = {}
percentage = {}
total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    csvheader = next(csvreader)
# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
    for index in csvreader:
        total_votes = total_votes + 1
#   * A complete list of candidates who received votes
        if index[2] in votecounter:
            votecounter[index[2]] += 1
        else:
            votecounter[index[2]] = 1
#   * The percentage of votes each candidate won
    for participant in votecounter:
        percentage[participant] = (votecounter[participant]/total_votes) * 100 
#print(percentage) test statement
        victory_count=0
        if votecounter[participant] > victory_count:

            vitory_count = votecounter[participant]
            
            victor = participant
   # print(f"the winner is {victor}") test statement
#   * The total number of votes each candidate won
    print("Elections Results")
    print("------------------------")
    print(f"Total Votes {total_votes}")
    print("------------------------")
    for each in votecounter:
        print(f"{each}:{percentage[each]:.3f}% {votecounter[each]}")
    print("------------------------")
    print(f"Winner: {victor}")
    print("------------------------")


#   * The winner of the election based on popular vote.
output_path = os.path.join('analysis','election_results.txt')
with open(output_path,"w") as new:
    new.write("Elections Results")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Votes {total_votes}")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    for each in votecounter:
        new.write(f"{each}:{percentage[each]:.3f}% {votecounter[each]}")
        new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Winner: {victor}")
    new.write("\n")
    new.write("------------------------")
