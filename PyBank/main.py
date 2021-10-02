# # # ## PyBank
import os
import csv
from typing import Collection

resource_path = os.path.join( "Resources", "budget_data.csv")

# ![Revenue](Images/revenue-per-lead.png)

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:


with open(resource_path, 'r') as csvfile:
    CSVreader = csv.reader(csvfile, delimiter = ',')
    header = next(CSVreader)
    #List entries in conlumb B
    colB1 = []
    #list containing the diffrenced between the months
    ProfDiff = [] 
    months_list = []
    monthstot = 0

# * The total number of months included in the dataset
    #months = len(list(CSVreader))
    #print(months)
    

#   
    for row in CSVreader:
        colB1.append(int(row[1]))
        months_list.append(row[0])
        monthstot += 1 
    # print(sum(colB))

#* The net total amount of "Profit/Losses" over the entire period
    tot_prof_loss = sum(colB1) 
#calculate the diffrences and put them into a list
    for entry in range(len(colB1)-1):
        
        ProfDiff.append(colB1[entry+1]-colB1[entry])
        
          
#print(ProfDiff)

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    average_diff = sum(ProfDiff)/len(ProfDiff)

#   * The greatest increase in profits (date and amount) over the entire period
    gre_increase = int(max(ProfDiff))
#   * The greatest decrease in profits (date and amount) over the entire period
    gre_decrease = min(ProfDiff)
   
    month_of_gre_inc = months_list[ProfDiff.index(gre_increase) + 1]
    month_of_gre_dec = months_list[ProfDiff.index(gre_decrease) + 1]


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{monthstot}")
print(f"Total: ${tot_prof_loss}")
print(f"Average Change: {round(average_diff)}")
print(f"Greatest Increase in Profits: {month_of_gre_inc} ${round(gre_increase)}")
print(f"Greatest Decrease in Profits: {month_of_gre_dec} ${round(gre_decrease)}")


txtpath = os.path.join('Analysis','Financial_Analysis.txt')
with open(txtpath,"w") as newoutput:
    newoutput.write("Financial Analysis")
    newoutput.write("\n")
    newoutput.write("------------------------")
    newoutput.write("\n")
    newoutput.write(f"Total Months:{monthstot}")a
    newoutput.write("\n")
    newoutput.write(f"Total: ${tot_prof_loss}")
    newoutput.write("\n")
    newoutput.write(f"Average Change: {round(average_diff)}")
    newoutput.write("\n")
    newoutput.write(f"Greatest Increase in Profits: {month_of_gre_inc} ${round(gre_increase)})")
    newoutput.write("\n")
    newoutput.write(f"Greatest Decrease in Profits: {month_of_gre_dec} ${round(gre_decrease)})")