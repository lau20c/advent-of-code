import os, time

with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r") as f:
    data = [int(line.strip()) for line in f]
data.sort(reverse=True)

def partOne(numbers):
    outer = 0
    while (outer < len(numbers)):
        inner = len(numbers)-1
        diff = 2020 - numbers[outer]
        while (inner >= 0):
            if (numbers[inner] == diff):
                break
            else:
                inner-=1
        if (numbers[outer]+numbers[inner] == 2020):
            print("Numbers: %i, %i" % (numbers[outer],numbers[inner]))
            print("Sum:", numbers[outer]+numbers[inner])
            print("Product:", numbers[outer]*numbers[inner])
            return
        else:
            outer+=1

def partTwo(numbers):
    index1 = 0
    while (index1 < len(numbers)):
        diff = 2020 - numbers[index1]
        index2 = len(numbers)-1
        while (index2 > 0):
            if (diff-numbers[index2-1] < 0):
                break
            else:
                index3 = index2-1
                while(index3 > 0):
                    if (diff-numbers[index2] == numbers[index3]):
                        print("Numbers: %i, %i, %i" % (numbers[index1], numbers[index2], numbers[index3]))
                        print("Sum:", numbers[index1]+numbers[index2]+numbers[index3])
                        print("Product:", numbers[index1]*numbers[index2]*numbers[index3])
                        return
                    else:
                        index3-=1
                index2-=1
        index1+=1

partOne(data)
partTwo(data)