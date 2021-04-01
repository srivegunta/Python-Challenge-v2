# First we'll import the os module - This will allow us to create file paths across operating systems
import os

# Reading using CSV module
import csv

# Read the CSV File 
dirname = os.path.dirname(__file__)
print (dirname)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')


#Define Variables: 
months = 0 # Count for total votes
netpnl = 0 # Net profit or loss
previous = 0 # Previous profit or loss
netchange = 0 # Net change in profit or loss
lastchange = 0 # Previous Net change in profit 
lastchange1 = 0 # Previous Net change in loss

# We can manipulate each element as we go

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        pnl = int(row[1]) #Set Profit and Loss column for Profit or Loss Amount
        months = months + 1 #Count to calculate Total Months 
        netpnl = netpnl + pnl #Net profit or loss variable - The net total amount of "Profit/Losses" over the entire period
        previous = pnl - previous #Previous Profit or Loss value for comparison

        if pnl == previous: 
            change = 0 #Set 0 value for the first row as there is no change
    
        else: 
            change = pnl - (pnl - previous) 
            netchange = (netchange + change)
            if lastchange > change: 
                maxchange = lastchange #The greatest increase in profits (date and amount) over the entire period
                lastchange = maxchange
            else: 
                maxchange = change 
                lastchange = maxchange #The greatest increase in profits (date and amount) over the entire period
                maxdate = row[0] #The greatest increase in profits (date) over the entire period

            if lastchange1 < change: 
                minchange = lastchange1
                lastchange1 = minchange #The greatest decrease in losses (date and amount) over the entire period
            else: 
                minchange = change
                lastchange1 = minchange #The greatest decrease in losses (date and amount) over the entire period
                mindate = row[0] #The greatest decrease in losses (date) over the entire period
        previous = pnl

avchange = format(netchange/(months-1),'.2f') # The average of the changes in "Profit/Losses" over the entire period

#Summary Table for Results on the Terminal       
print("Financial Analysis")
print("--------------------------")
print(f"Total Months : {months}")
print(f"Total: ${netpnl}")
print(f"Average Change: ${avchange}")
print(f"Greatest Increase in Profits: {maxdate} (${maxchange})")
print(f"Greatest Decrease in Profits: {mindate} (${minchange})")

#Specify the file to write to
PyBank_Summary = os.path.join(dirname, 'analysis',"PyBank_Summary.txt")

# Write the txt file
with open(PyBank_Summary, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months : {months}\n")
    txtfile.write(f"Total: ${netpnl}\n")
    txtfile.write(f"Average Change: ${avchange}\n")
    txtfile.write(f"Greatest Increase in Profits: {maxdate} (${maxchange})\n")
    txtfile.write(f"Greatest Decrease in Profits: {mindate} (${minchange})\n")

