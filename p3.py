
Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\p3\p3.txt"

def LoadAndProcessInput(filepath, Part1 = True):
    input = open(filepath).readlines()
    input = [x.strip() for x in input]
    if Part1:
        input = [[x[:int(len(x)/2)], x[int(len(x)/2):]] for x in input]
    return input    

def LocateCommonElement(rucksack):
    #There should only be 1 intersection
    return list(set(rucksack[0]).intersection(set(rucksack[1])))[0]

def MapCharacterToIntValue(value):
    if value.lower() == value:
        return ord(value) - 96
    else:
        return ord(value) - 64 + 26    
    
def SolutionPart1(filepath):
    input = LoadAndProcessInput(filepath)
    scorePart1 = 0
    for rucksack in input:
        commonElement = LocateCommonElement(rucksack)
        scorePart1 += MapCharacterToIntValue(commonElement)
    return scorePart1    

def SolutionPart2(filepath):
    input = LoadAndProcessInput(filepath, Part1 = False)
    scorePart2 = 0
    for i in range(0,len(input),3):
        commonElement = list(set(input[i]).intersection(set(input[i+1]), set(input[i+2])))[0]
        scorePart2 += MapCharacterToIntValue(commonElement)
    return scorePart2    
        


        
print("The Solution to Part 1 is: ", SolutionPart1(Filepath))
print("The Solution to Part 2 is: ", SolutionPart2(Filepath))


