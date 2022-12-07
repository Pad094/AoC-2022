



Filepath = r"C:\Development\AdventOfCode\2022\P1\P1.txt"


def GetElfData(filepath):
    testData = []
    inputFile = open(filepath, 'r').readlines()
    for line in inputFile:
        if line == '\n':
            testData.append(-1)
        else:    
            testData.append(int(line))
    return testData        


def SolvePart1(filepath):
    elfData = GetElfData(filepath)
    elfAmounts = []
    newElf = 0
    for i in range(len(elfData)):
        if elfData[i] == -1 or i == len(elfData):
            elfAmounts.append(newElf)
            newElf = 0
        else:
            newElf +=  elfData[i] 
    return max(elfAmounts)


def SolvePart2(filepath):
    elfData = GetElfData(filepath)
    elfAmounts = []
    newElf = 0
    for i in range(len(elfData)):
        if elfData[i] == -1 or i == len(elfData):
            elfAmounts.append(newElf)
            newElf = 0
        else:
            newElf +=  elfData[i] 
    elfAmounts = sorted(elfAmounts)        
    return sum(elfAmounts[-3:])



print("The Solution to part 1: ", SolvePart1(Filepath))
print("The Solution to part 2: ", SolvePart2(Filepath))