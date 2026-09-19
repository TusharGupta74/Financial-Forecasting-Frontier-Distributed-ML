#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    # Skip header and malformed rows
    if not row or row[0] == "age" or len(row) < 17:
        continue

    try:
        month = row[10].strip()
        subscription = row[16].strip()

        print("{}\t{}".format(month, subscription))

    except IndexError:
        continue