"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# Create dictionary to record time user spent on their phone
telephone_call_time = {}

for call in calls:
    # Add caller record
    if call[0] in telephone_call_time:
        telephone_call_time[call[0]] += int(call[3])
    else:
        telephone_call_time[call[0]] = int(call[3])

    # Add receiver record
    if call[1] in telephone_call_time:
        telephone_call_time[call[1]] += int(call[3])
    else:
        telephone_call_time[call[1]] = int(call[3])

telephone_longest = max(telephone_call_time, key=telephone_call_time.get)
longest_time = telephone_call_time[telephone_longest]

print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(telephone_longest, longest_time))
