import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    financial_data = csv.reader(csvfile, delimiter=',')

    print(financial_data)

    header = next(financial_data)

    print(f"Header:  {header}")

    max_profit = 0
    max_loss = 0
    total_months = 0
    plsum = 0.0

    for row in financial_data:
        print(row)

        total_months += 1
        profit_loss = int(row[1])
        plsum += profit_loss
        if profit_loss > max_profit:
            max_profit = profit_loss
        elif profit_loss < max_loss:
            max_loss = profit_loss

    average_change = int(plsum / total_months)

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {int(plsum)}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {max_profit}")
    print(f"Greatest Decrease in Profits: {max_loss}")

