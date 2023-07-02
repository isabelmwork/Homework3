import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_rows = 0
#stores candidate name, votes, percentage of votes
candidate_info = {}
#stores candidate names
candidate_list = []

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #move to header
    next(csvreader)

    for row in csvreader:
        
        total_rows += 1

        #candidate name is in the 3rd column of election_data.csv
        candidate_name = row[2]

        #finds number of votes each candidate got
        if candidate_name in candidate_info:
            
            #candidate exists in dict
            candidate_info[candidate_name] += 1

        else:

            #candidate doesnt exist in dict, add them to dict
            candidate_info[candidate_name] = 1
            
            candidate_list.append(candidate_name)
    
    #function for finding percentage of votes each candidate in candidate_list got
    #adds the percentage of votes to the candidate in dict
    def percentage_of_votes(candidate_name, total_votes):

        #calculate percentage
        candidate_votes = candidate_info[candidate_name]
        percentage = round((candidate_votes/total_votes) * 100, 3)

        #add info to dict
        candidate_info[candidate_name] = [candidate_info[candidate_name], percentage]

    print("\nElection Results\n---------------------------\nTotal Votes: " + str(total_rows) + "\n---------------------------")

    #make first candidate the winner for future comparisons
    winner_votes = candidate_info[candidate_list[0]]

    for i in range(len(candidate_list)):
       
        #finds percentage of votes each candidate got and updates dict 
        percentage_of_votes(candidate_list[i], total_rows)

        if winner_votes < candidate_info[candidate_list[i]][0]:
            
            #finds election winner
            winner_votes = candidate_info[candidate_list[i]][0]
            winner_name = candidate_list[i]

        #prints candidate info nicely
        print(candidate_list[i] + ": " + str(candidate_info[candidate_list[i]][1]) + "% (" + str(candidate_info[candidate_list[i]][0]) + ")")

    print("---------------------------\nWinner: " + winner_name + "\n---------------------------\n\n")

#write txt
file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:
    
    txt_file.write("\nElection Results\n---------------------------\nTotal Votes: " + str(total_rows) + "\n---------------------------\n")

    for i in range(len(candidate_list)):

        txt_file.write(candidate_list[i] + ": " + str(candidate_info[candidate_list[i]][1]) + "% (" + str(candidate_info[candidate_list[i]][0]) + ")\n")

    txt_file.write("---------------------------\nWinner: " + winner_name + "\n---------------------------\n\n")





