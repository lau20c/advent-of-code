import os
import math

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    data = [list(line.strip()) for line in f]


def partOne(passes):
    seats = []
    for ticket in passes:
        i = row = col = 0
        dist = [0, 127]
        while i < len(ticket):
            # calculate row first
            if ticket[i] == 'B' or ticket[i] == 'R':
                dist = [math.ceil((dist[0]+dist[-1])/2), dist[-1]]
            else:
                dist = [dist[0], math.floor((dist[0]+dist[-1])/2)]
            i += 1
            # reset distance to calculate column
            if i == 7:
                row = dist[0]
                dist = [0, 7]
        col = dist[0]
        # calculate and append seatID
        seats.append((row*8)+col)
    return(max(seats))


def partTwo(passes):
    occupied = []
    for ticket in passes:
        i = row = col = 0
        dist = [0, 127]
        while i < len(ticket):
            # calculate row first
            if ticket[i] == 'B' or ticket[i] == 'R':
                dist = [math.ceil((dist[0]+dist[-1])/2), dist[-1]]
            else:
                dist = [dist[0], math.floor((dist[0]+dist[-1])/2)]
            i += 1
            # reset distance to calculate column
            if i == 7:
                row = dist[0]
                dist = [0, 7]
        col = dist[0]
        # calculate and append seatID
        occupied.append((row*8)+col)
    occupied.sort()
    # remove very front and back seats
    for seat in occupied:
        if seat <= (0*8)+7 or seat >= (127*8)+0:
            occupied.remove(seat)
    # find free seat
    i = 1
    while i < len(occupied) - 1:
        if not (occupied[i-1] + 1 == occupied[i]
                and occupied[i] == occupied[i+1]-1):
            return(occupied[i]+1)
        i += 1


print(partOne(data))
print(partTwo(data))
