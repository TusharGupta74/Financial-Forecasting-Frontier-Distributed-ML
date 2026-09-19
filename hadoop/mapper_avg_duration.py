import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if len(row) != 17:
        continue

    if row[0] == "age":
        continue

    try:
        duration = float(row[11])
        poutcome = row[15]

        print("{}\t{}".format(poutcome, duration))
    except ValueError:
        continue