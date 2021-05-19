import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

def PyFinancial(file):

    with open(csvpath, 'r') as csvfile:

        financial_data = csv.reader(csvfile, delimiter=',')
        header = next(financial_data)

        max_profit = 0
        max_loss = 0
        total_months = 0
        pl_sum = 0.0
        pl_start = 0.0

        for row in financial_data:
            total_months += 1
            profit_loss = int(row[1])
            month = str(row[0])
            pl_sum += profit_loss

            if profit_loss > max_profit:
                max_profit = profit_loss
                max_month = month
            elif profit_loss < max_loss:
                max_loss = profit_loss
                min_month = month
        
            if total_months == 1:
                pl_start = profit_loss
        
            pl_end = profit_loss

        pl_change = pl_end - pl_start
        average_change = round(pl_change / total_months, 2)

        print("Financial Analysis")
        print("------------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${int(pl_sum)}")
        print("Average Change: $" + "{:.2f}".format(round(average_change,2)))
        print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
        print(f"Greatest Decrease in Profits: {min_month} (${max_loss})")

output_path = os.path.join("analysis", "bank_analysis.txt")

output = str(PyFinancial(csvpath))

with open(output_path, 'w') as txtfile:
    txtfile.write(output)