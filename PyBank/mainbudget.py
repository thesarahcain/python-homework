import os
import csv
x = os.path.join("Resources", "budget_data.csv")
month_count = 0
out_put_folder = "Analysis"
output_file = os.path.join(out_put_folder, "Final_budget_analysis.txt")

month_differences = []
net_change_list = []
net_total = 0
max_increase_month = ""
max_increase_amount = float("-inf")
min_increase_month = ""
min_increase_amount = float("inf")
with open(x, "r") as y:
    budget_data = csv.reader(y)
    header = next(budget_data)
    first_row = next(budget_data)
    month_count += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])
    for i in budget_data:
        month_count += 1
        net_total += int(i[1])
        net_change = int(i[1]) - prev_net
        prev_net = int(i[1])
        net_change_list += [net_change]
        month_differences += [i[0]]
        if net_change >max_increase_amount: 
            max_increase_amount = net_change 
            max_increase_month = i[0]
        if net_change < min_increase_amount: 
            min_increase_amount = net_change
            min_increase_month = i[0]
difference = sum(net_change_list) / len(net_change_list)
rounded_difference = round(difference,2)
print(f"Total Months:{month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${rounded_difference}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount})")
print(f"Greatest Decrease in Profits: {min_increase_month} (${min_increase_amount})")
print("Results exported to Final_budget_analysis.txt")


with open(output_file, "w") as output_file:
    output_file.write(f"Financial Analysis\n")
    output_file.write(f"----------------------------\n")
    output_file.write(f"Total Months: {month_count}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${rounded_difference}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {min_increase_month} (${min_increase_amount})\n")

print(f"Analysis is written to {output_file}")

    













