import os

with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r") as f:
    data = [int(line.strip()) for line in f]
data.sort(reverse=True)

def partOne(numbers):
    i = 0
    while (i < len(numbers)):
        diff = 2020 - numbers[i]
        if diff in numbers:
            print("Numbers: %i, %i" % (numbers[i], diff))
            print("Sum:", numbers[i]+diff)
            print("Product:", numbers[i]*diff)
            return
        else:
            i+=1

def partTwo(numbers):
    i1 = 0
    while (i1 < len(numbers)):
        diff = 2020 - numbers[i1]
        i2 = len(numbers)-1
        while (i2 > 0):
            diff2 = diff-numbers[i2]
            if (diff2 < 0):
                break
            else:
                if diff2 in numbers:
                    print("Numbers: %i, %i, %i" % (numbers[i1], numbers[i2], diff2))
                    print("Sum:", numbers[i1]+numbers[i2]+diff2)
                    print("Product:", numbers[i1]*numbers[i2]*diff2)
                    return
                else:
                    i2-=1
        i1+=1

partOne(data)
partTwo(data)