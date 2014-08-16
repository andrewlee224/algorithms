import sys
from random import choice

# Random contraction algorithm
# Use to find minimum cut of a graph
# May need repeated tries to find the smallest cut

def removeAll(l, v):
  return [ item for item in l if item != v ]

def countMinCut(resultDict):
  return len((list(resultDict.values()))[0])

def createVertexDict(f):
  vertexDict = {}

  for line in f:
    splitLine = line.split()
    key = (int(splitLine[0]),) 
    adjacentVertices = [ (int(element), ) for element in splitLine[1:] ]
    vertexDict[key] = adjacentVertices

  return vertexDict


def RContraction(originVertexDict):

  vertexDict = originVertexDict.copy()
  numVertices = len(vertexDict.keys())

  while (numVertices > 2):
    # choose random edge
    randomSuperVertex = choice(list(vertexDict.keys())) 
    mergingVertex = choice(vertexDict[randomSuperVertex])
    mergingSuperVertex = [ tup for tup in vertexDict.keys() if mergingVertex[0] in tup ][0]
    resultingSuperVertex = randomSuperVertex + mergingSuperVertex
    resultingAdjacentVertices = vertexDict[randomSuperVertex] + vertexDict[mergingSuperVertex]
    
    # delete original vertices from dict
    vertexDict.pop(randomSuperVertex, None)
    vertexDict.pop(mergingSuperVertex, None)
    # remove self-loops
    for vertex in randomSuperVertex:
      resultingAdjacentVertices = removeAll(resultingAdjacentVertices, (vertex, ))
    for vertex in mergingSuperVertex:
      resultingAdjacentVertices = removeAll(resultingAdjacentVertices, (vertex, ))
    
    # add new super-vertex to dict
    vertexDict[resultingSuperVertex] = resultingAdjacentVertices
   
    numVertices = numVertices - 1


  return vertexDict


def batchContraction(fName, numRepeats):
    vertexDict = createVertexDict(open(fName, 'r'))

    minCutEdges = float('inf')
    minCutDict = {}

    for i in range(numRepeats):
        print("Iteration {}".format(i))
        resultDict = RContraction(vertexDict)
        cutEdges = len(resultDict[resultDict.keys()[0]])
        if cutEdges < minCutEdges:
            minCutEdges = cutEdges
            minCutDict = resultDict

    return minCutDict, minCutEdges


if __name__ == '__main__':
    filename = sys.argv[1]
    numRepeats = int(sys.argv[2])

    minCutDict, minCutEdges = batchContraction(filename, numRepeats)
  
    print("Minimum cut found with {} edges".format(minCutEdges))
