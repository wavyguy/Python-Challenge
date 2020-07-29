import os
import csv
from pathlib import Path

csvpath = os.path.join('..', 'Resources', 'budgetdata.csv')


#Set Outputs 
month = []
revenue =[]
revenue_change = []

#Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
   #Go Through Rows in File 
    for row in csvreader:
        month.append(row[0])
        revenue.append(int(row[1]))


    #Monthly Change in Revenue
    for i in range(len(revenue)-1):
        revenue_change.append(revenue[i+1]-revenue[i])


#Minimum and Maximum Revenue Changes
max_increase_revenue = max(revenue_change)
max_decrease_revenue = min(revenue_change)


#Max and Min Increase Indexes
max_increase_month = revenue_change.index(max(revenue_change)) + 1
max_decrease_month = revenue_change.index(min(revenue_change)) + 1


#Print Summary Table 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(revenue)}")
print(f"Average Change: ${round(sum(revenue_change)/len(revenue_change),2)}")
print(f"Greatest Increase in Profits: {month[max_increase_month]} (${(str(max_increase_revenue))})")
print(f"Greatest Decrease in Profits: {month[max_decrease_month]} (${(str(max_decrease_revenue))})")



#Actions to Place Onto Text File
output = Path("..", "PyBank", "Financial_Analysis_Summary.txt")

with open(output,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(month)}")
    file.write("\n")
    file.write(f"Total: ${sum(revenue)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(revenue_change)/len(revenue_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month[max_increase_month]} (${(str(max_increase_revenue))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month[max_decrease_month]} (${(str(max_decrease_revenue))})")

