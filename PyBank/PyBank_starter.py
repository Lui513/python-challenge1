# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = [] 
average_change = 0
greatest_increase = 0
greatest_increase_date = 0
greatest_decrease = 0
greatest_decrease_date = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Track the total and net change


    # Process each row of data
    for row in reader:
        

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if int(row[1]) > previous_net:
           greatest_increase = int(row[1]) 
           greatest_increase_date = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        elif int(row[1]) < previous_net:
            greatest_decrease = int(row[1]) 
            greatest_decrease_date = row[0]



# Calculate the average net change across the months
average_change = sum(net_change_list) / total_months

# Generate the output summary


# Print the output
print(f"Financial Analysis\n")
print(f"------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: $ {total_net}\n")
print(f"Average Change: ${round(average_change)}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}\n")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: $ {total_net}\n")
    txt_file.write(f"Average Change: ${round(average_change)}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}\n")

