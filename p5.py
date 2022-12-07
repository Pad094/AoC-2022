
#Input stacks
stack1 = ['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N']
stack2 = ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G']
stack3 = ['L', 'Q', 'V']
stack4 = ['N', 'B', 'S', 'W', 'R', 'Q']
stack5 = ['N', 'D', 'F', 'T', 'V', 'M', 'B']
stack6 = ['M', 'D', 'B', 'V', 'H', 'T', 'R']
stack7 = ['D', 'B', 'Q', 'J']
stack8 = ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q']
stack9 = ['B', 'N', 'H', 'M', 'S']


Stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
import copy

Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\p5\p5.txt"

def LoadInInstrucations(filepath):
    file = open(filepath).readlines()
    instructions = []
    for line in file:
        if line[0] == 'm':
            nextInstruction = line.split(" ")
            instructions.append([int(nextInstruction[1]), int(nextInstruction[3]),  int(nextInstruction[5].strip())])
    return instructions




def SolutionPart1(filepath, stacks):
    instructions =  LoadInInstrucations(filepath)
    for i in range(len(instructions)):
        for j in range(instructions[i][0]):
            nextPop = stacks[instructions[i][1]-1].pop()
            stacks[instructions[i][2] -1].append(nextPop)

    tops = ""
    for i in range(len(stacks)):
        tops += stacks[i].pop()
    return tops 



def SolutionPart2(filepath, stacks):
    instructions =  LoadInInstrucations(filepath)
    for i in range(len(instructions)):
        nextMove =[]
        for j in range(instructions[i][0]):
            nextMove.append(stacks[instructions[i][1]-1].pop())
        nextMove = nextMove[::-1]
        stacks[instructions[i][2] -1] = stacks[instructions[i][2] -1] + nextMove

    tops = ""
    for i in range(len(stacks)):
        tops += stacks[i].pop()
    return tops        


print("Solution to Part 1: ", SolutionPart1(Filepath, copy.deepcopy(Stacks)))
print("Solution to Part 2: ", SolutionPart2(Filepath, copy.deepcopy(Stacks)))

