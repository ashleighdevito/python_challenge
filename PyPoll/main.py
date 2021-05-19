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
        percents_list = ["{:.3%}".format(votes / total_votes) for votes in vote_list]
        vote_formatted = ' '.join('({})'.format(vote) for vote in vote_list)
        victor = max(candidate_dic, key = lambda key: candidate_dic[key])

        result_summary = zip(candidate_list, percents_list, vote_formatted)

        print(candidate_list)
        print(vote_list)
        print(percents_list)
        print(vote_formatted)
        print(candidate_dic)
        print(victor)

        print("Election Results")
        print("---------------------")
        print(f"Total Votes: {total_votes}")
        print("---------------------")
        print(result_summary)
        print("---------------------")
        print(f"Winner: {victor}")






