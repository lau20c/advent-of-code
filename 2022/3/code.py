from pathlib import Path

import csv
from collections import Counter

'''
Mapping
a-z : 1-26
A-Z : 27-52

Unicode
a-z : 97 - 122
-96
A-Z : 65 - 90
-38
'''

rucksacks = Path('input.csv').read_text().splitlines()

# Part 1
total1 = 0 
for sack in rucksacks:
    midpoint = len(sack)//2
    comp_1 = Counter(sack[:midpoint])
    comp_2 = Counter(sack[midpoint:])
    dupe = list((comp_1 & comp_2).keys())[0]
    priority = ord(dupe) - 96 if dupe.islower() else ord(dupe) - 38
    total1 += priority

# Part 2
total2 = 0
group = []
for sack_num in range(1, len(rucksacks)+1):
    group.append(rucksacks[sack_num - 1])
    if sack_num % 3 == 0:
        badge = list(Counter(group[0]) & Counter(group[1]) & Counter(group[2]))[0]
        priority = ord(badge) - 96 if badge.islower() else ord(badge) - 38
        total2 += priority
        group = []

print(F"Part one: {total1}")
print(F"Part two: {total2}")