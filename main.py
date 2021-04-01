# First we'll import the os module - This will allow us to create file paths across operating systems
import os

# Reading using CSV module
import csv

# Read the CSV File 
dirname = os.path.dirname(__file__)
print (dirname)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')

#Define Variables: 
count = 0 # Count for total votes
candidate1 = "Unsure" # Idenitfier for First Candidate
candidate2 = "Unsure" # Idenitfier for Second Candidate 
candidate3 = "Unsure" # Idenitfier for Third Candidate
candidate4 = "Unsure" # Idenitfier for Fourth Candidate
count1 = 0 # Count for total votes for the First Candidate
count2 = 0 # Count for total votes for the Second Candidate
count3 = 0 # Count for total votes for the Third Candidate
count4 = 0 # Count for total votes for the Fourth Candidate

# We can manipulate each element as we go

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Assign counts(votes) and Candidate names for a summary table of candidates - complete list of candidates who received votes

    for row in csvreader:
        count = count + 1
        candidate = str(row[2]) 
        if candidate1 == "Unsure":
            candidate1 = candidate
            count1 = count1+ 1
        elif candidate == candidate1:
            count1 = count1+ 1
        elif candidate2 == "Unsure":
            candidate2 = candidate 
            count2 = count2+1
        elif candidate == candidate2:
            count2 = count2+ 1    
        elif candidate3 == "Unsure":
            candidate3 = candidate 
            count3 = count3+1
        elif candidate == candidate3:
            count3 = count3+ 1  
        elif candidate4 == "Unsure":
            candidate4 = candidate 
            count4 = count4+1  
        else: 
            count4 = count4 + 1

# Identify the Candidate with the highest votes - winner of the election based on popular vote

if count1 > count2:
    winner = candidate1
elif count2 > count3:
    winner = candidate2 
elif count3 > count4:  
    winnner = candidate3
else:
    winner = candidate4      

# Calculate percentage of votes each candidate won

cand1_perc = "{:.3%}".format(count1/count)    
cand2_perc = "{:.3%}".format(count2/count)    
cand3_perc = "{:.3%}".format(count3/count)    
cand4_perc = "{:.3%}".format(count4/count)        
      
#Summary Table for Results on the Terminal       
print("Election Results")
print("--------------------------")
print(f"Total Votes : {count}")
print("--------------------------")
print(f"{candidate1}: {cand1_perc} ({count1})")
print(f"{candidate2}: {cand2_perc} ({count2})")
print(f"{candidate3}: {cand3_perc} ({count3})")
print(f"{candidate4}: {cand4_perc} ({count4})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Specify the file to write to
Pypoll_summary = os.path.join(dirname, 'analysis','PyPoll_Summary.txt')

# Write the Summary results to the txt file
with open(Pypoll_summary, 'w') as txtfile:
     txtfile.write("Election Results\n")
     txtfile.write("-------------------------\n")
     txtfile.write(f"Total Votes : {count}\n")
     txtfile.write("-------------------------\n")
     txtfile.write(f"{candidate1}: {cand1_perc} ({count1})\n")
     txtfile.write(f"{candidate2}: {cand2_perc} ({count2})\n")
     txtfile.write(f"{candidate3}: {cand3_perc} ({count3})\n")
     txtfile.write(f"{candidate4}: {cand4_perc} ({count4})\n")
     txtfile.write("-------------------------\n")
     txtfile.write(f"Winner: {winner}\n")
     txtfile.write("-------------------------\n")

