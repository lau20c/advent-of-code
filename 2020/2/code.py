import os

with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r") as f:
    data = [(line.strip().split()) for line in f]

def partOne(passwords):
    count = 0
    for line in passwords:
        arrayRange = line[0].split("-") # isolate range
        validRange = range(int(arrayRange[0]), int(arrayRange[1])+1)
        targetChar = line[1].strip(':') # isolate target letter
        if (line[2].count(targetChar) in validRange):
            count+=1
    return count

def partTwo(passwords):
    count = 0
    for line in passwords:
        arrayIndices = list(map(lambda x: int(x)-1, line[0].split("-")))
        targetChar = line[1].strip(':') # isolate target letter
        positives = 0
        for index in arrayIndices:
            if line[2][index] == targetChar:
                positives+=1
        if positives == 1:
            count+=1
    return count

print(partOne(data))
print(partTwo(data))