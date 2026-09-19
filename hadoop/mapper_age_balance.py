import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if len(row) != 17:
        continue

    if row[0] == "age":
        continue

    try:
        age = int(row[0])
        balance = float(row[5])

        if age < 30:
            age_group = "<30"
        elif age < 40:
            age_group = "30-39"
        elif age < 50:
            age_group = "40-49"
        elif age < 60:
            age_group = "50-59"
        else:
            age_group = "60+"

        print("{}\t{}".format(age_group, balance))

    except ValueError:
        continue