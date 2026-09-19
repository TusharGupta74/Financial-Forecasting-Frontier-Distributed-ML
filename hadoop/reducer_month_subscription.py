#!/usr/bin/env python3

import sys

current_month = None
total_clients = 0
yes_count = 0
no_count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    month, subscription = line.split("\t", 1)

    if current_month == month:
        total_clients += 1

        if subscription == "yes":
            yes_count += 1
        elif subscription == "no":
            no_count += 1

    else:
        if current_month is not None:
            print("{}\ttotal={}\tyes={}\tno={}".format(
                current_month,
                total_clients,
                yes_count,
                no_count
            ))

        current_month = month
        total_clients = 1
        yes_count = 1 if subscription == "yes" else 0
        no_count = 1 if subscription == "no" else 0

if current_month is not None:
    print("{}\ttotal={}\tyes={}\tno={}".format(
        current_month,
        total_clients,
        yes_count,
        no_count
    ))