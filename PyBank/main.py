import os
import csv

csvpath = os.path.join("/Users/sergioescobedo/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_amount = 0
    months_count = 0
    previous_value = None
    average_change = 0
    greatest_increase = float("-1000000")
    greatest_decrease = float("1000000")
    greatest_increase_month = ""
    greatest_decrease_month = ""

    for i, row in enumerate(csvreader, start=1):
        if i > 0:
            value = float(row[1])
            total_amount += value
            months_count += 1

            if previous_value is not None:
                change = value - previous_value
                average_change += change

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_month = row[0]
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_month = row[0]

            previous_value = value

    average_change /= (months_count - 1)

with open(os.path.join("/Users/sergioescobedo/Desktop/python-challenge/PyBank/Analysis","analysis.txt" ), "a+") as my_file:
    my_file.write("Financial Analysis\n")
    my_file.write("-------------------------------\n")
    my_file.write(f"Total amount: {total_amount}\n")
    my_file.write(f"Total months: {months_count}\n")
    my_file.write(f"Average change: {average_change}\n")
    my_file.write(f"Greatest increase: {greatest_increase} ({greatest_increase_month})\n")
    my_file.write(f"Greatest decrease: {greatest_decrease} ({greatest_decrease_month})\n")

    print("Financial Analysis\n")
    print("-------------------------------")
    print(f"Total amount: {total_amount}")
    print(f"Total months: {months_count}")
    print(f"Average change: {average_change}")
    print(f"Greatest increase: {greatest_increase} ({greatest_increase_month})")
    print(f"Greatest decrease: {greatest_decrease} ({greatest_decrease_month})")
 




    




    


        