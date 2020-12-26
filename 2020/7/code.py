import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    data = [(line.strip()) for line in f]


def partOne(rules, target):
    validColors = []
    inProgress = True
    while inProgress:  # run until an iteration completes with no new validColors
        startingSize = len(validColors)
        for rule in rules:
            parent = rule.split(" bags contain ")[0]
            children = rule.split(" bags contain ")[1]
            if parent not in validColors:       # look at children
                if children.count(target) > 0:  # holds target directly
                    validColors.append(parent)
                else:                           # holds target indirectly
                    for color in validColors:
                        if children.count(color) > 0:
                            validColors.append(parent)
                            break
        if startingSize == len(validColors):
            inProgress = False
    return len(validColors)


def partTwo(rules, target):
    for rule in rules:
        parent = rule.split(" bags contain ")[0]
        if parent == target:  # find target
            print(rule)
            print(rule.split(" bags contain ")[1])
            break


dummy = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    #'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags, 8 shiny gold bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]

#partOne(dummy, "shiny gold")
print(partOne(data, "shiny gold"))
partTwo(data, "shiny gold")
