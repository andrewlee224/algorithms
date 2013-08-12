'''
Dijkstra's shortest path algorithm
'''

import sys

def createVertexDict(filename):
  f = open(filename)
  vertexDict = {}
  line = f.readline()

  while line != '':
    splitLine = line.split()
    adjacentVertices = []

    for i in range(1, len(splitLine)):
      splitAgain = splitLine[i].split(',')
      vertexTuple = (int(splitAgain[0]), int(splitAgain[1]))
      adjacentVertices.append(vertexTuple)

    vertexDict[int(splitLine[0])] = adjacentVertices
    line = f.readline()

  return vertexDict

def shortestPaths(vertexDict, source):
  explored = set()


if __name__ == '__main__':
  filename = sys.argv[1]
  vertexDict = createVertexDict(filename)
