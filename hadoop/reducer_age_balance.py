import sys

current_group = None
total_balance = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        age_group, balance = line.split("\t")
        balance = float(balance)
    except ValueError:
        continue

    if current_group == age_group:
        total_balance += balance
        count += 1
    else:
        if current_group is not None:
            average = total_balance / count
            print("{}\tcount={}\tavg_balance={:.2f}".format(
                current_group, count, average
            ))

        current_group = age_group
        total_balance = balance
        count = 1

if current_group is not None:
    average = total_balance / count
    print("{}\tcount={}\tavg_balance={:.2f}".format(
        current_group, count, average
    ))