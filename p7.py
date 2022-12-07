Filepath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\2022\p7\p7.txt"

class node:
    def __init__(self, name, depth, parent):
        self.Name = name
        self.Depth = depth
        self.Parent = parent
        self.Children = []
        self.Size = 0

    def __repr__(self) -> str:
        return self.Name

    def __hash__(self):
        return hash(repr(self))

    def AddChild(self, childNode):
        self.Children.append(childNode)    

    def AddFileSize(self, size):
        self.Size =size

#We append integers to files to distinguish between files of same name in different directories.
def SwitchToAppropriateChild(parentNode, childName):
    nameLength = len(childName)
    for child in parentNode.Children:
        if child.Name[:nameLength] == childName:
            try:
                    int(child.Name[nameLength:])
                    return child
            except:
                continue  


def BuildGraphFromInputFile(filepath):
    file = open(filepath).readlines()

    rootNode =  node('root', 0, None)
    NodeDepths = [[]]
    NodeDepths[0].append(rootNode)
    nodeDictionary = {'root': rootNode}     

    currentParent = rootNode
    nodeCount = 0

    for line in file:
        if line[0] == "$": #command
            if line[2] == "c": #change directory
                if line[5] == '/': #move back to root
                    nodeDictionary[currentParent.Name] = currentParent
                    currentParent = rootNode
                elif line[5]   == "." and  line[6] == '.': #move back a level
                    nodeDictionary[currentParent.Name] = currentParent
                    currentParent = currentParent.Parent
                else: # switch down a directory
                    nodeDictionary[currentParent.Name] = currentParent
                    currentParent = SwitchToAppropriateChild(currentParent, line.strip().split()[-1])
   
                    
            elif line[2] == "l": #list
                pass

            else:
                raise Exception("Unknown Value")
        else:
            if line[0] == 'd': # directory
                nextNodeName = line.strip().split()[-1] + str(nodeCount)
                nodeCount += 1
                nextNode = node(nextNodeName, depth = currentParent.Depth + 1, parent= currentParent)
                nodeDictionary[nextNodeName] = nextNode
                currentParent.AddChild(nextNode)
                try:
                    NodeDepths[currentParent.Depth + 1].append(nextNode)
                except:
                    NodeDepths.append([])
                    NodeDepths[currentParent.Depth + 1].append(nextNode)    

            else:
                nextNodeName = line.strip().split()[-1] + str(nodeCount)
                nodeCount += 1
                nextNode = node(nextNodeName, depth = currentParent.Depth + 1, parent= currentParent)
                size = int(line.strip().split(" ")[0])
                nextNode.AddFileSize(size)
                currentParent.AddChild(nextNode)
                nodeDictionary[nextNodeName] = nextNode
                try:
                    NodeDepths[currentParent.Depth + 1].append(nextNode)
                except:
                    NodeDepths.append([])
                    NodeDepths[currentParent.Depth + 1].append(nextNode)


    #Add the node sizes
    for i in range(len(NodeDepths)-2, -1, -1):
        for currentNode in NodeDepths[i]:
           if nodeDictionary[currentNode.Name].Children != []:
                children = nodeDictionary[currentNode.Name].Children
                size = 0
                for child in children:
                    size = size + child.Size        
                nodeDictionary[currentNode.Name].AddFileSize(size)  
    return nodeDictionary  


def SolutionPart1(filepath):
    nodeDictionary = BuildGraphFromInputFile(filepath)
    fileSizes = 0
    for file in nodeDictionary.keys():
        if nodeDictionary[file].Size <= 100000 and nodeDictionary[file].Children != []:
            fileSizes += nodeDictionary[file].Size
    return fileSizes

def SolutionPart2(filepath):
    nodeDictionary = BuildGraphFromInputFile(filepath)

    sizeToBeat = 30000000 - (70000000 - nodeDictionary['root'].Size)
    currentMinimum = 100000000

    for key in nodeDictionary.keys():
        if (nodeDictionary[key].Size >= sizeToBeat) and (nodeDictionary[key].Size - sizeToBeat < currentMinimum) and (nodeDictionary[key].Children != []):
            currentMinimum = nodeDictionary[key].Size - sizeToBeat   

    return currentMinimum + sizeToBeat 



print("The Solution to Part 1 is: ", SolutionPart1(Filepath))
print("The Solution to Part 2 is: ", SolutionPart2(Filepath))
