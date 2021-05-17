import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

def PyBank_Analysis (financial_data):
    month = financial_data[0]
    profit_loss = financial_data[1]

    total_months = len(month)

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {}")
    print(f"Greatest Decrease in Profits: {}")
    

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

output_file = os.path.join("output.csv")
