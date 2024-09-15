"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Requirement here is to identify different telephone numbers, for this part
# Set data type can be used to identifyunique elements from texts and calls list

different_numbers = set()

# Sort through texts list and add both sender and receiver telephone numbers
for text in texts:
    different_numbers.add(text[0]) #Sender telephone number
    different_numbers.add(text[1]) #Receiver telephone number

# Sort through calls list and add both caller and receiver telephone numbers
for call in calls:
    different_numbers.add(call[0]) #Caller telephone number
    different_numbers.add(call[1]) #Receiver telephone number

print("There are {} different telephone numbers in the records.".format(len(different_numbers)))
