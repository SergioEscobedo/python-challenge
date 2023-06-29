import os
import csv

csvpath = os.path.join("/Users/sergioescobedo/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    total_count = 0
    counts = {}
    max_percentage = 0
    max_candidate = ""

    for row in csvreader:
        candidate = row[2]
        if candidate in counts:
            counts[candidate] += 1
        else:
            counts[candidate] = 1
        total_count += 1
    
    print("Election Results")
    print("------------------")
    print(f"Total votes: {total_count}")
    print("------------------")

    with open(os.path.join("/Users/sergioescobedo/Desktop/python-challenge/PyPoll/Analysis", "analysis.txt"), "a+") as my_file:
        my_file.write("Election Results\n")
        my_file.write("------------------\n")

        for candidate, count in counts.items():
            percentage = (count / total_count) * 100
            result = f"{candidate}: ({count} votes), {percentage:.2f}%\n"
            my_file.write(result)
            print(result, end="") 

            if percentage > max_percentage:
                max_percentage = percentage
                max_candidate = candidate

        my_file.write("------------------\n")
        winner_result = f"Winner: {max_candidate} {max_percentage:.2f}%\n"
        my_file.write(winner_result)
        print(winner_result, end="")