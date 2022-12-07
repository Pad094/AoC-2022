


Filepath = r"C:\Development\AdventOfCode\2022\p6\p6.txt"

def SolutionPart1(filepath):
    input = open(filepath).readlines()[0]
    slider = list(input[:4])
    i = 3
    while True:
        if len(set(slider)) == 4:
            return i+1
        else:
            i = i+1    
            del slider[0]
            slider.append(input[i])


def SolutionPart2(filepath):
    input = open(filepath).readlines()[0]
    slider = list(input[:14])
    i = 13
    while True:
        if len(set(slider)) == 14:
            return i+1
        else:
            i = i+1    
            del slider[0]
            slider.append(input[i])            
    
        





print("The solution to Part 1 is: ", SolutionPart1(Filepath))
print("The solution to Part 2 is: ", SolutionPart2(Filepath))

