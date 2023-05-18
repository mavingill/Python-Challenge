#Dependencies
import csv

file_to_load = 'budget_data.csv'
file_to_output = 'analysis/budget_analysis.txt'

#Track various Revenue Parameters
total_months = 0
previous_revenue = 0
month_of_change = []
change_of_revenue_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 999999999999999]
total_revenue = 0

#Read csv and convert to list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    #Track totals
    for row in reader:
        total_months += 1
        total_revenue += int(row['Profit/Losses'])
        
        #Track Revenue Change
        revenue_change = int(row['Profit/Losses']) - previous_revenue
        previous_revenue = int(row['Profit/Losses'])
        change_of_revenue_list.append(revenue_change)
        month_of_change.append(row['Date'])
        
        #Greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row['Date']
            greatest_increase[1] = revenue_change

            
        #Greatest decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row['Date']
            greatest_decrease[1] = revenue_change

            
#Average Revenue Change
revenue_avg = sum(change_of_revenue_list[1:]) / len(change_of_revenue_list[1:])


#output
output = (
    f'\nFinancial Analysis\n'
    f'---------------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total Revenue: ${total_revenue}\n'
    f'Average Revenue Change: ${revenue_avg:.2f}\n'
    f'Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
)

print(output)

with open(file_to_output, 'w') as txt_file:
    txt_file.write(output)
