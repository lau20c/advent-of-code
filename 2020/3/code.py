import os

with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r") as f:
    data = [list(line.strip()) for line in f]

def treeCount(forest, xStep, yStep):
    index = trees = rows = 0
    for line in forest:
        if ((rows != 0) and (rows % yStep != 0)): # vertical movement
            rows += 1
        else:
            if (index > len(line)-1): # reset index if we're at the end of the line
                index = index - len(line)
            if line[index] == '#': # check location for tree
                trees +=1
            index += xStep # horizontal movement
            rows += 1
        
        if (rows == len(forest)): # exit if we're at the bottom
            return trees

print("Part 1: ", treeCount(data, 3, 1))
print("Part 2: ", 
    treeCount(data, 1, 1)*
    treeCount(data, 3, 1)*
    treeCount(data, 5, 1)*
    treeCount(data, 7, 1)*
    treeCount(data, 1, 2))

