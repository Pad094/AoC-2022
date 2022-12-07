
Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\P2\p2.txt"

def PreprocessData(filepath):
    input = open(filepath).readlines()
    roundArray = []
    for i in range(len(input)):
        round = input[i].strip().split()
        roundArray.append([round[0], round[1]])

    return roundArray


def SolvePart1(filepath):
    input = PreprocessData(filepath)
    results = []
    for round in input:
        score = 0
        if round[0] == 'A':
            if round[1] == 'X':
                score +=3
            elif round[1] == 'Y':
                score += 6

        elif round[0] == 'B':
            if round[1] == 'Y':
                score += 3
            elif round[1] == 'Z':
                score += 6    
        else:
            if round[1] == 'Z':
                score += 3
            elif round[1] == 'X':
                score += 6 

        if round[1] == 'X':
            score += 1
        elif round[1] == 'Y':
            score +=2
        else:
             score +=3  

        results.append(score)   
    return sum(results)                      

def SolvePart2(filepath):
    input = PreprocessData(filepath)
    results = []
    for round in input:
        score = 0
        if round[0] == 'A':
            if round[1] == 'X':
                score +=3
            elif round[1] == 'Y':
                score += 4
            else:
                score += 8    

        elif round[0] == 'B':
            if round[1] == 'X':
                score += 1
            elif round[1] == 'Y':
                score += 5
            else:
                score += 9        
        else:
            if round[1] == 'X':
                score += 2
            elif round[1] == 'Y':
                score += 6
            else:
                score += 7     
 

        results.append(score)   
    return sum(results)

print("Solution to Part 1: ", SolvePart1(Filepath))
print("Solution to Part 2: ", SolvePart2(Filepath))


