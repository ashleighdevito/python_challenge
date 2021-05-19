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

        
        print(candidate_dic)
