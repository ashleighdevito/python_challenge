import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

def PyBank_Analysis (financial_data):
    month = financial_data[0]
    profit_loss = financial_data[1]
    plsum = 0.0
    plchange = []

    total_months = len(month)

    for row in profit_loss:
        plsum += profit_loss


    for row in profit_loss:
        change = row - (row - 1)
        plchange.append(change)

    def average_change(list):
        length = len(list)
        total = 0.0
        for number in list:
            total += number
        return total / length

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_months}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")
    
print(PyBank_Analysis)

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

output_file = os.path.join("output.csv")
