

Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\p8\p8.txt"

def ProcessFileInput(filepath):
    matrixInput = []
    input = open(filepath).readlines()
    for line in input:
        line = line.strip()
        matrixInput.append([int(x) for x in line])
    return matrixInput


def ReturnVisibleTreeCount(grid):
    gridLength = len(grid)
    gridWidth  = len(grid[0])
    indicatorVisibilityGrid = [[0 for x in range(gridWidth)] for y in range(gridLength)]
    
    #Left Side:
    for i in range(gridLength):
        currentHeight = -1
        for j in range(gridWidth):
            if grid[i][j] > currentHeight:
                indicatorVisibilityGrid[i][j] = 1
                currentHeight = grid[i][j]        

    #RightSide:
    for i in range(gridLength):
        currentHeight = -1
        for j in range(gridWidth-1, -1, -1):
            if grid[i][j] > currentHeight:
                indicatorVisibilityGrid[i][j] = 1
                currentHeight = grid[i][j] 
            
    #Top:
    for i in range(gridWidth):
        currentHeight = -1
        for j in range(gridLength):
            if grid[j][i] > currentHeight:
                indicatorVisibilityGrid[j][i] = 1
                currentHeight = grid[j][i] 
          
    #Bottom:
    for i in range(gridLength):
        currentHeight = -1
        for j in range(gridWidth-1, -1, -1):
            if grid[j][i] > currentHeight:
                indicatorVisibilityGrid[j][i] = 1
                currentHeight = grid[j][i] 

    return indicatorVisibilityGrid   

def CalculateScenicScoreForTree(grid, xcoord, ycoord):
    gridLength = len(grid)
    gridWidth  = len(grid[0])
    


    #top
    top = 0
    for i in range(xcoord-1, -1, -1):
        if grid[i][ycoord] < grid[xcoord][ycoord]:
            top += 1
        else:
             top += 1
             break

    #bottom
    bottom = 0
    for i in range(xcoord+1, gridLength):
        if grid[i][ycoord] < grid[xcoord][ycoord]:
            bottom += 1
        else:
             bottom += 1
             break

    #left
    left = 0
    for i in range(ycoord-1, -1, -1):
        if grid[xcoord][i] < grid[xcoord][ycoord]:
            left += 1
        else:
             left += 1
             break

    #left
    right = 0
    for i in range(ycoord+1, gridWidth):
        if grid[xcoord][i] < grid[xcoord][ycoord]:
            right += 1
        else:
             right += 1
             break

    return top*bottom*left*right



def CalculateScenicScore(grid):
    gridLength = len(grid)
    gridWidth  = len(grid[0])
    scenicScoreGrid = [[0 for x in range(gridWidth)] for y in range(gridLength)]

    maxScenicScore = 0
    for i in range(gridLength):
        for j in range(gridWidth):
            if maxScenicScore < CalculateScenicScoreForTree(grid, i, j):
                maxScenicScore =  CalculateScenicScoreForTree(grid, i, j)
    return maxScenicScore



def SolutionPart1(filepath):
    input = ProcessFileInput(filepath)   
    visibilityGrid = ReturnVisibleTreeCount(input)
    return sum([sum(x) for x in visibilityGrid ])


def SolutionPart2(filepath):
    input = ProcessFileInput(filepath)
    return CalculateScenicScore(input)


print("The Solution to Part 1 is: ", SolutionPart1(Filepath))
print("The Solution to Part 2 is: ", SolutionPart2(Filepath))

