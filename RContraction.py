import sys
import pdb
from random import randint, choice

def createVertexDict(f):
  vertexDict = {}

  for line in f:
    splitLine = line.split()
    key = int(splitLine[0]) 
    adjacentVertices = [ int(element) for element in splitLine[1:] ]
    vertexDict[key] = adjacentVertices

  return vertexDict

def RContraction(originVertexDict):

  vertexDict = originVertexDict.copy()
  verticesList = [ (element,) for element in vertexDict.keys() ]
  numVertices = len(vertexDict.keys())
  vertexSum = len(vertexDict)

  while (numVertices > 2):
    # pdb.set_trace()
    try:
      randomVertexTuple = choice(verticesList)     # randomVertexTuple - might be merged - a tuple
      randomVertex = choice(randomVertexTuple)
      randomDestination = choice(vertexDict[randomVertex])      # also vertex - both vertices constitute an edge
    except:
      e, m, tb = sys.exc_info()
      pdb.post_mortem(tb)
      
    mergingVertexTuple = [ tup for tup in verticesList if randomDestination in tup ][0]      # dest vertex might be a part of merged vertex
    newVertexTuple = tuple(set(randomVertexTuple + mergingVertexTuple))
    
    # delete both merged vertices and add their sum to the vertices list
    verticesList.remove(randomVertexTuple)
    verticesList.remove(mergingVertexTuple)
    verticesList.append(newVertexTuple)
    
    # delete links to second vertex (all values from tuple) from first vertex entry in vertexDict and vice-versa
    for vertex1 in randomVertexTuple:
      for vertex2 in mergingVertexTuple:
        if vertex1 in vertexDict[vertex2]:
          vertexDict[vertex2].remove(vertex1)
        if vertex2 in vertexDict[vertex1]:
          vertexDict[vertex1].remove(vertex2)

        if not vertexDict[vertex2]:
          print("Deleting vertex2 from verticesList: ")
          emptyVertexTuples = []
          emptyVertexTuples = [ tup for tup in verticesList if vertex2 in tup ]
          if not emptyVertexTuples:
            break
          emptyVertexTuple = emptyVertexTuples[0]
          emptyVertexList = list(emptyVertexTuple)
          emptyVertexList.remove(vertex2)
          newVertexTuple = tuple(emptyVertexList)
          verticesList.remove(emptyVertexTuple)
          verticesList.append(newVertexTuple)
          print([item for item in verticesList if vertex2 in item])

        if not vertexDict[vertex1]:
          print("Deleting vertex2 from verticesList: ")
          emptyVertexTuples = []
          emptyVertexTuple = [ tup for tup in verticesList if vertex1 in tup ]
          if not emptyVertexTuples:
            break
          emptyVertexTuple = emptyVertexTuples[0]
          emptyVertexList = list(emptyVertexTuple)
          emptyVertexList.remove(vertex1)
          newVertexTuple = tuple(emptyVertexList)
          verticesList.remove(emptyVertexTuple)
          verticesList.append(newVertexTuple)
          print([item for item in verticesList if vertex1 in item])



    numVertices = numVertices - 1

  count = 0
  for tailVertex in verticesList[0]:
     count = count + len(vertexDict[tailVertex])

  return (verticesList, vertexDict, count)

if __name__ == '__main__':
  filename = sys.argv[1]
  f = open(filename)

  vertexDict = createVertexDict(f)
