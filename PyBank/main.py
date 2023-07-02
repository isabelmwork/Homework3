import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_rows = 0

total_profit_loss = 0

previous_row = []
change_profit_loss = 0
total_change_profit_loss = 0
average_change_profit_loss = 0

amount_greatest_increase = 0
date_greatest_increase = ""
amount_greatest_decrease = 0
date_greatest_decrease = ""

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #move to header
    next(csvreader)

    #move to first row and save it
    previous_row = next(csvreader)

    total_profit_loss = int(previous_row[1])

    total_rows += 1

    for row in csvreader:
        
        total_rows += 1

        total_profit_loss += int(row[1])
        
        #update total_change_profit_loss
        change_profit_loss = 0 
        change_profit_loss = int(row[1]) - int(previous_row[1])
        total_change_profit_loss += change_profit_loss

        #update greatest increase in profit
        if change_profit_loss > amount_greatest_increase:

            amount_greatest_increase = change_profit_loss
            date_greatest_increase = str(row[0])

        #update greatest decrease in profit
        if  change_profit_loss < amount_greatest_decrease:

            amount_greatest_decrease = change_profit_loss
            date_greatest_decrease = str(row[0])

        #save current row to previous_row
        previous_row = row

    average_change_profit_loss = round(total_change_profit_loss/(total_rows - 1), 2)

    print("\nFinancial Analysis\n---------------------------\nTotal Months: " + str(total_rows) + 
          "\nTotal: $" + str(total_profit_loss) + 
          "\nAverage Change: $" + str(average_change_profit_loss) + 
          "\nGreatest Increase in Profits: " + date_greatest_increase + 
          " ($" + str(amount_greatest_increase) + ")" +
          "\nGreatest Decrease in Profits: " + date_greatest_decrease +
          " ($" + str(amount_greatest_decrease) + ")\n")

    #write txt
    file_to_output = os.path.join("analysis", "election_analysis.txt")

    with open(file_to_output, "w") as txt_file:
    
        txt_file.write("\nFinancial Analysis\n---------------------------\nTotal Months: " + str(total_rows) + 
            "\nTotal: $" + str(total_profit_loss) + 
            "\nAverage Change: $" + str(average_change_profit_loss) + 
            "\nGreatest Increase in Profits: " + date_greatest_increase + 
            " ($" + str(amount_greatest_increase) + ")" +
            "\nGreatest Decrease in Profits: " + date_greatest_decrease +
            " ($" + str(amount_greatest_decrease) + ")\n")

