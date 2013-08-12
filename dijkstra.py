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

def createEdgeList(filename):
  f = open(filename)
  edgeList = []
  line = f.readline()
  vertexSet = set()

  while line != '':
    splitline = line.split()
    src = int(splitline[0])
    if src not in vertexSet:
      vertexSet.add(src)

    for i in range(1, len(splitline)):
      splitAgain = splitline[i].split(',')
      dest = int(splitAgain[0])
      cost = int(splitAgain[1])
      if splitAgain[0] not in vertexSet:
        vertexSet.add(dest)
      edgeList.append((src, dest, cost))
    
    line = f.readline()

  return (edgeList, vertexSet)
  

def shortestPaths(edgeList, vertexSet, source):
  explored = { source }
  minimumCost = { source : 0 }
  numVertices = len(vertexSet)

  while len(explored) != numVertices: 
    # for every explored vertex get candidate edges
    candidateEdge = (None, None, 1000000)

    for (src, dest, cost) in edgeList:
      if src in explored and dest not in explored:
        if not candidateEdge[0]:
          candidateEdge = (src, dest, cost)
        elif (minimumCost[src] + cost) < (minimumCost[candidateEdge[0]] + candidateEdge[2]):
          candidateEdge = (src, dest, cost)

    explored.add(candidateEdge[1])
    minimumCost[candidateEdge[1]] = minimumCost[candidateEdge[0]] + candidateEdge[2]

  return minimumCost


if __name__ == '__main__':
  filename = sys.argv[1]
  edgeList, vertexSet = createEdgeList(filename)
  minCost = shortestPaths(edgeList, vertexSet, 1)
