import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    data = [(line.strip()) for line in f]


def cleanData(input):
    cleansedData = []
    temp = ""
    for line in input:
        if (line == ''):
            cleansedData.append(temp.split())
            # cleansedData.append(createPair(temp.split()))
            temp = ""
        else:
            temp += (line + " ")
    else:
        cleansedData.append(temp.split())
        # cleansedData.append(createPair(temp.split()))
    return cleansedData


def partOne(answers):
    total = 0
    for group in answers:
        groupAnswers = ""
        for person in group:
            groupAnswers += person
        gradedAnswers = set(groupAnswers)
        total += len(gradedAnswers)
    return(total)


def partTwo(answers):
    total = 0
    for group in answers:
        groupAnswers = {}
        peopleCnt = 0
        for person in group:
            for question in person:
                if question in groupAnswers.keys():
                    groupAnswers[question] += 1
                else:
                    groupAnswers[question] = 1
            peopleCnt += 1
        gradedAnswers = [
            q for q in groupAnswers.keys() if peopleCnt == groupAnswers[q]]
        total += len(gradedAnswers)
    return(total)


cleansedData = cleanData(data)
print(partOne(cleansedData))
print(partTwo(cleansedData))
