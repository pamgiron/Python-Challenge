#Importing all programs to run code
import csv
import os

#Printing out fin. analysis 
print("Financial Analysis" + "\n" + "\n" + "--------------------------")

#import csv file using os path 
csvpath = os.path.join("Resources","budget_data.csv")

#Create list of Total months
Months =[]
TotalMnth = 0
Change = 0
Avgchge = 0
Increase = 0
Decrease = 0

#open csv file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#Append months
    for row in csvreader:
        month = row[0]
        Months.append(month)
#Create net total amount of profit/losses

        profit = int(row[1])
        TotalMnth = TotalMnth + profit
#Find changes in profit/losses and average 
        if row[1] != 0:
            Change = Change + int(row[1])
#find greatest Increase change 
            if int(Change) > Increase:
                Increase = int(Change)
                day = str(row[0])
            
            if int(Change) < Decrease:
                Decrease = int(Change)
                days = str(row[0])

            Avgchge = Avgchge + Change
            Change = -int(row[1])
#Find greatest Decrease change
            

#Print results
print("Total Months: " + str(int(len(Months)-1)) + "\n" )
print("Total: $" + str(int(TotalMnth)) + "\n")
print("Average Change: $" + str(format(float((Avgchge - 1088983)/(int(len(Months))-2)), '.2f')) +"\n")
print("Greatest Increase in Profits: " + str(day) + " ($" + str(Increase) +") ")
print("Greatest Decrease in Profits: " + str(days) + " ($" + str(Decrease) +") " )

#declare variables to include as outputs for file export
aa = "Financial Analysis" + "\n" + "\n" + "--------------------------"
bb = "Total Months: " + str(int(len(Months)-1)) + "\n"
cc = "Average Change: $" + str(format(float((Avgchge - 1088983)/(int(len(Months))-2)), '.2f')) +"\n"
dd = "Greatest Increase in Profits: " + str(day) + " ($" + str(Increase) +") "
ee = "Greatest Decrease in Profits: " + str(days) + " ($" + str(Decrease) +") "

#write a with statement to add file to analysis folder - Python_Analysis
with open ( "Analysis/Python_Analysis", "w") as file:
    #Use variables to write lines
    lines = ([aa,bb,cc,dd,ee])
    file.writelines(lines)