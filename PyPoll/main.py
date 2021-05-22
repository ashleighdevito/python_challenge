#import dependancies
import os
import csv

#define import path for data
csvpath = os.path.join('Resources', 'election_data.csv')

#open the datafile
with open(csvpath, 'r') as csvfile:

    #definte a variable for the data
    poll_data = csv.reader(csvfile, delimiter=',')
    
    #assign first row of data as a header
    header = next(poll_data)

    #initialize the variable to count the votes
    total_votes = 0

    #create a dictionary to store the named candidates
    candidate_dic = {}

    #read through csv 
    for row in poll_data:
        #identify vote to which candidate
        candidate = row[2]

        #counting total votes
        total_votes += 1

        #for each vote, add new candidate to dictionary or add vote to current cantidate tally
        candidate_dic[str(candidate)] = candidate_dic.get(str(candidate), 0) + 1

    #define lists to store candidates, how many respective votes
    candidate_list = list(candidate_dic)
    vote_list = list(candidate_dic.values())

    #define a list of candidates percentage of total votes
    percents_list = ["{:.3%}".format(votes / total_votes) for votes in vote_list]

    #define winner as the candidate with most number of votes
    victor = max(candidate_dic, key = lambda key: candidate_dic[key])

    #zip together lists of candidates, their vote percentage, and vote count
    result_summary = zip(candidate_list, percents_list, vote_list)
    
    #print analysis to terminal
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------------")
    for cl,pl,vl in result_summary:
        print(f'{cl}: {pl} ({vl})')
    print("------------------------------")
    print(f"Winner: {victor}")

#identify where to open a results file
output_path = os.path.join("analysis", "election_analysis.txt")
    
#open the file of where to print output
with open(output_path, 'w') as txtfile:
    
    #zip together the three lists defined above
    result_summary = zip(candidate_list, percents_list, vote_list)

    #print the header and number of total votes as text
    txtfile.write(
        "Election Results\n"
        "------------------------------\n"
        f"Total Votes: {total_votes}\n"
        "------------------------------\n")

    #print results for each candidate
    for cl,pl,vl in result_summary:
        txtfile.write(f'{cl}: {pl} ({vl})\n')

    #print the winning candidate    
    txtfile.write(
        "------------------------------\n"
        f"Winner: {victor}\n")