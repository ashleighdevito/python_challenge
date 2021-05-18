import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    financial_data = csv.reader(csvfile, delimiter=',')

    header = next(financial_data)

    def PyBank_Analysis (financial_data):
        month = financial_data[0]
        profit_loss = financial_data[1]
        max_profit = 0
        max_loss = 0
        total_months = 0
        plsum = 0.0

        for row in financial_data:
            total_months += 1
    
        print(total_months)

        for row in financial_data:
            plsum += profit_loss

        print(plsum)

        for row in financial_data:
            if profit_loss > max_profit:
                max_profit = profit_loss

        print(max_profit)

        for row in financial_data:
            if profit_loss < max_loss:
                max_loss = profit_loss

        print(max_loss)

        average_change = plsum / total_months

        print("Financial Analysis")
        print("---------------------")
        print(f"Total Months: {total_months}")
        print(f"Average Change: {average_change}")
        print(f"Greatest Increase in Profits: {max_profit}")
        print(f"Greatest Decrease in Profits: {max_loss}")
    
    
print(PyBank_Analysis)
