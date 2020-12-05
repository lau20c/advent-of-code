import os, re

with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r") as f:
    data = [(line.strip()) for line in f]

def createDictionary(unprocessed):
    processed = {}
    for item in unprocessed:
        splitItem = item.split(':')
        processed.update({splitItem[0]:splitItem[1]})
    return processed

cleansedData = []
temp = ""
for line in data:
    if (line==''):
        cleansedData.append(createDictionary(temp.split()))
        temp=""
    else:
        temp += (line + " ")
else:
    cleansedData.append(createDictionary(temp.split()))
    
def partOne(collection):
    validPassports = 0
    for passport in collection:
        print(passport)
        if (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
            validPassports += 1
    return validPassports

tests = {
    "byr": range(1920, 2003),
    "iyr": range(2010, 2021),
    "eyr": range(2020, 2031),
    "hgt": {"cm": range(150, 194), "in": range(59, 77)},
    "hcl": "^#(([0-9]*[a-f]*)*){6}",
    "ecl": ["amb","blu","brn","gry","grn","hzl","oth"],
    "pid": "[0-9]{9}",
}

def partTwo(collection, checks):
    validPassports = 0
    for passport in collection:
        copy = passport.copy()
        if "cid" in copy:
            del copy['cid']

        if (copy.keys() == checks.keys()):
            print("PASSPORT: ", passport)
            valid = True
            for key, value in passport.items():
                if key == "pid":
                    if not re.search(checks[key], value):
                        print("PID: wrong")
                        valid = False
                        break 
                    print("PID: correct")
                elif key == "hgt":
                    if not re.search("[0-9]?[0-9][0-9](cm|in){1}$", value):
                        print("HGT: wrong")
                        valid = False
                        break
                    else:
                        unit = value[-2:]
                        num = int(value[:-2])
                        if num not in checks[key][unit]:
                            print("HGT: wrong")
                            valid = False
                            break 
                        print("HGT: correct")
                elif key == "hcl":
                    if re.search(checks[key], value):
                        print("HCL: correct")
                        continue
                    else:
                        print("HCL: wrong")
                        valid = False
                        break
                elif key == "cid":
                    print(key, ": unnecessary")
                    continue
                elif key == "ecl":
                    if value not in checks[key]:
                        print(key, ": wrong")
                        valid = False
                        break
                    print(key, ": correct")
                else:
                    if int(value) not in checks[key]:
                        print(key, ": wrong")
                        valid = False
                        break
                    print(key, ": correct")
            print(valid)
            if valid:
                print("added")
                validPassports +=1
    return validPassports
    

# print(partOne(cleansedData))
print(partTwo(cleansedData, tests))