#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    # Skip header and malformed rows
    if not row or row[0] == "age" or len(row) < 6:
        continue

    try:
        job = row[1].strip()
        balance = float(row[5])
        print("{}\t{}".format(job, balance))
    except (ValueError, IndexError):
        continue