import csv
from collections import Counter

ans1, ans2 = 0, 0
with open('input.csv', newline='') as input:
    csv_reader = csv.reader(input, delimiter=',')
    for row in csv_reader:
        range1 = [int(x) for x in row[0].split('-')]
        sections1 = list(range(range1[0],range1[1]+1))

        range2 = [int(x) for x in row[1].split('-')]
        sections2 = list(range(range2[0],range2[1]+1))

        combined = set(sections1 + sections2)
        if len(combined) == len(sections1) or len(combined) == len(sections2):
            ans1 += 1
            
        if Counter(sections1) & Counter(sections2):
            ans2 += 1

print(f"Part one: {ans1}")
print(f"Part two: {ans2}")