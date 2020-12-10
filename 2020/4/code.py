import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    data = [(line.strip()) for line in f]


def createPair(unprocessed):
    processed = {}
    for item in unprocessed:
        splitItem = item.split(':')
        processed.update({splitItem[0]: splitItem[1]})
    return processed


def cleanData(input):
    cleansedData = []
    temp = ""
    for line in input:
        if (line == ''):
            cleansedData.append(createPair(temp.split()))
            temp = ""
        else:
            temp += (line + " ")
    else:
        cleansedData.append(createPair(temp.split()))
    return cleansedData


def partOne(collection):
    validPassports = 0
    for passport in collection:
        if (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
            validPassports += 1
    return validPassports


tests = {
    "byr": range(1920, 2003),
    "iyr": range(2010, 2021),
    "eyr": range(2020, 2031),
    "hgt": {"hgt": "^[0-9]?[0-9][0-9](cm|in){1}$",
            "cm": range(150, 194),
            "in": range(59, 77)},
    "hcl": "^#(([0-9]*[a-f]*)*){6}$",
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": "^[0-9]{9}$",
}


def partTwo(collection, checks):
    validPassports = 0
    for passport in collection:
        copy = passport.copy()
        if "cid" in copy:
            del copy['cid']
        if (copy.keys() == checks.keys()):  # check that all required fields are present
            valid = True
            for key, value in passport.items():  # validate fields
                if key == "cid":
                    continue
                elif key == "hgt":
                    if not re.search(checks[key][key], value):
                        valid = False
                        break
                    else:
                        unit = value[-2:]
                        num = int(value[:-2])
                        if num not in checks[key][unit]:
                            valid = False
                            break
                elif key == "pid" or key == "hcl":
                    if not re.search(checks[key], value):
                        valid = False
                        break
                elif key == "ecl":
                    if value not in checks[key]:
                        valid = False
                        break
                else:
                    if int(value) not in checks[key]:
                        valid = False
                        break
            if valid:
                validPassports += 1
    return validPassports


cleansedData = cleanData(data)
print(partOne(cleansedData))
print(partTwo(cleansedData, tests))
