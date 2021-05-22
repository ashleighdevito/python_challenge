#import dependacies
import os
import csv

#define import path for data
csvpath = os.path.join('Resources', 'budget_data.csv')

#define the function to perform the analysis
def PyBank():

    #open the data file
    with open(csvpath, 'r') as csvfile:

        #define variable to store data, specify delimiter
        financial_data = csv.reader(csvfile, delimiter=',')

        #assign first row of data as a header
        header = next(financial_data)

        #initialize variables to store 
        #   greatest increase
        #   greatest decrease
        #   total months
        #   running sum of profit/loss
        #   starting profit/loss
        max_profit = 0
        max_loss = 0
        total_months = 0
        pl_sum = 0.0
        pl_start = 0.0

        #read each row of data
        for row in financial_data:
            #add each row to month count
            total_months += 1

            #store current row of data as current month and profit/loss
            month = str(row[0])
            profit_loss = int(row[1])
            
            #running sum of profit/loss
            pl_sum += profit_loss

            #compare stored variables for greatest increase and decrease to current row
            #   if greater value, store new value and month
            if profit_loss > max_profit:
                max_profit = profit_loss
                max_month = month
            elif profit_loss < max_loss:
                max_loss = profit_loss
                min_month = month
        
            #store starting value of profit/loss
            if total_months == 1:
                pl_start = profit_loss
        
            #store ending value of profit/loss
            pl_end = profit_loss

        #calculate change in profit/loss over the time period
        pl_change = pl_end - pl_start
        average_change = (pl_change / total_months)
        
        #format average change and store as string
        average_delta = ("%.2f" % average_change)

        #define a variable to output
        output = (
        "Financial Analysis\n"
        "------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${int(pl_sum)}\n"
        f"Average Change: $ {average_delta}\n"
        f"Greatest Increase in Profits: {max_month} (${max_profit})\n"
        f"Greatest Decrease in Profits: {min_month} (${max_loss})\n"
        )

        #
        return output

#print output to terminal
analysis = PyBank()
print(analysis)

#identify path to store output text file
output_path = os.path.join("analysis", "bank_analysis.txt")

#print output of function into output file
with open(output_path, 'w') as txtfile:
    analysis = PyBank()
    txtfile.writelines(analysis)