#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    # Skip header and malformed rows
    if not row or row[0] == "age" or len(row) < 7:
        continue

    try:
        education = row[3].strip()
        housing = row[6].strip()

        print("{}\t{}".format(education, housing))

    except IndexError:
        continue