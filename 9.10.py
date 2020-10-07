#Anthony Guzman           9.1          CIS2348
import csv

filename = input()

f = open(filename)
csvreader = csv.reader(f)
words = next(csvreader)

count = {}

for word in words:
    if word.strip() in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

for k, v in count.items():
    print(k, v)