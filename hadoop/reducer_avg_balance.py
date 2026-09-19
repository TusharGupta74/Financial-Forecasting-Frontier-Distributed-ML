#!/usr/bin/env python3

import sys

current_job = None
total_balance = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    job, balance = line.split("\t", 1)
    balance = float(balance)

    if current_job == job:
        total_balance += balance
        count += 1
    else:
        if current_job is not None:
            average = total_balance / count
            print("{}\t{:.2f}".format(current_job, average))

        current_job = job
        total_balance = balance
        count = 1

if current_job is not None:
    average = total_balance / count
    print("{}\t{:.2f}".format(current_job, average))