#!/usr/bin/env python3

import sys

current_education = None
yes_count = 0
no_count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    education, housing = line.split("\t", 1)

    if current_education == education:
        if housing == "yes":
            yes_count += 1
        elif housing == "no":
            no_count += 1

    else:
        if current_education is not None:
            print("{}\tyes={}\tno={}".format(
                current_education,
                yes_count,
                no_count
            ))

        current_education = education
        yes_count = 1 if housing == "yes" else 0
        no_count = 1 if housing == "no" else 0

if current_education is not None:
    print("{}\tyes={}\tno={}".format(
        current_education,
        yes_count,
        no_count
    ))