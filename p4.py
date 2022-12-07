

Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\p4\p4.txt"

def LoadAndPreprocessData(filepath):
    input = open(filepath).readlines()
    boundaries = []
    for line in input:
        nextCommand = line.replace("-", ",").split(",")
        nextCommand[-1] = nextCommand[-1].strip()
        nextCommand = [int(x) for x in nextCommand]
        boundaries.append(nextCommand)
    return boundaries


def SolvePart1(filepath):
    instructions = LoadAndPreprocessData(filepath)
    dominationCount = 0
    for instruction in instructions:
        if instruction[0] <= instruction[2] and instruction[1] >= instruction[3]:
            dominationCount += 1
        elif  instruction[0] >= instruction[2] and instruction[1] <= instruction[3]: 
            dominationCount += 1
    return dominationCount   

def SolvePart2(filepath):
    instructions = LoadAndPreprocessData(filepath)
    overlapCount = 0
    for instruction in instructions:
        if instruction[0] <= instruction[2] and instruction[1] >= instruction[2]:
            overlapCount += 1
        elif  instruction[0] <= instruction[3] and instruction[1] >= instruction[3]: 
            overlapCount += 1
        elif instruction[0] >= instruction[2] and instruction[1] <= instruction[3]:
            overlapCount += 1

    return overlapCount           


print("The solution to Part 1 is: ", SolvePart1(Filepath))
print("The solution to Part 2 is: ", SolvePart2(Filepath))

