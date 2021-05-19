import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

        poll_data = csv.reader(csvfile, delimiter=',')
        header = next(poll_data)

        total_votes = 0
        candidate_dic = {}

        for row in poll_data:
            candidate = row[2]
            total_votes += 1
            candidate_dic[str(candidate)] = candidate_dic.get(str(candidate), 0) + 1

        print(total_votes)

        candidate_list = list(candidate_dic)
        vote_list = list(candidate_dic.values())
        percents_list = ["%.3f"% ((votes / total_votes) * 100) for votes in vote_list]

        print(candidate_list)
        print(vote_list)
        print(percents_list)
        print(candidate_dic)

        print("Election Results")
        print("---------------------")
        print(f"Total Votes: {total_votes}")
        print("---------------------")

        print("---------------------")
        print(f"Winner: {victor}")






