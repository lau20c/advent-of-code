import os
import math

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    data = [list(line.strip()) for line in f]


def partOne(passes):
    seats = []
    for ticket in passes:
        i = 0
        row = [0, 127]
        col = [0, 7]
        while i < len(ticket):
            if i < 7:
                if ticket[i] == 'B':
                    row = [math.ceil((row[0]+row[-1])/2), row[-1]]
                else:
                    row = [row[0], math.floor((row[0]+row[-1])/2)]
            else:
                if ticket[i] == 'R':
                    col = [math.ceil((col[0]+col[-1])/2), col[-1]]
                else:
                    col = [col[0], math.floor((col[0]+col[-1])/2)]
            i += 1
        seats.append((row[0]*8)+col[0])
    return(max(seats))

# def process(input):
#     output = []
#     for line in input:
#         output.append(list(line))
#     return output


examples = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

# print(process(examples))
print(partOne(data))
