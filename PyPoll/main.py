import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

def PyPoll():

    with open(csvpath, 'r') as csvfile:

        poll_data = csv.reader(csvfile, delimiter=',')
        header = next(poll_data)

        total_votes = 0
        candidate_dic = {}

        for row in poll_data:
            candidate = row[2]
            total_votes += 1
            candidate_dic[str(candidate)] = candidate_dic.get(str(candidate), 0) + 1

        candidate_list = list(candidate_dic)
        vote_list = list(candidate_dic.values())
        percents_list = ["{:.3%}".format(votes / total_votes) for votes in vote_list]
        victor = max(candidate_dic, key = lambda key: candidate_dic[key])

        result_summary = zip(candidate_list, percents_list, vote_list)
        
        print("Election Results")
        print("------------------------------")
        print(f"Total Votes: {total_votes}")
        print("------------------------------")
        for cl,pl,vl in result_summary:
            print(f'{cl}: {pl} ({vl})')
        print("------------------------------")
        print(f"Winner: {victor}")

        output = (
        "Election Results\n"
        "------------------------------\n"
        f"Total Votes: {total_votes}\n"
        "------------------------------\n"
        for cl,pl,vl in result_summary:
            print(f'{cl}: {pl} ({vl})')
        "------------------------------\n"
        f"Winner: {victor}\n")

        return output
        
output_path = os.path.join("analysis", "election_analysis.txt")
    
with open(output_path, 'w') as txtfile:
    analysis = PyPoll()
    txtfile.writelines(analysis)