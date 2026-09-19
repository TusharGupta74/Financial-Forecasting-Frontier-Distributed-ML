import sys

current_outcome = None
total_duration = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        outcome, duration = line.split("\t")
        duration = float(duration)
    except ValueError:
        continue

    if current_outcome == outcome:
        total_duration += duration
        count += 1
    else:
        if current_outcome is not None:
            average = total_duration / count
            print("{}\t{:.2f}".format(current_outcome, average))

        current_outcome = outcome
        total_duration = duration
        count = 1

if current_outcome is not None:
    average = total_duration / count
    print("{}\t{:.2f}".format(current_outcome, average))