import sys

def createEdgeList(filename):
  f = open(filename)
  edgeList = [ (int(line.split()[0]), int(line.split()[1])) for line in f ]
  
  return edgeList

def DFSftimes(edgeList, vertex, explored, ftimes, t): 
  explored.add(vertex)

  # explore every reversed edge
  for (tail, head) in edgeList:
    if head == vertex and tail not in explored:
      t = DFSftimes(edgeList, tail, explored, ftimes, t)
  
  t = t+1
  ftimes[vertex] = t

  return t

def DFSleaders(edgeList, ftimes, vertex, source, explored, leaders):
  explored.add(vertex)
  leaders[vertex] = source

  for (tail, head) in edgeList:
    tailAlias = ftimes[tail]
    headAlias = ftimes[head]
    if tailAlias == vertex and headAlias not in explored:
      DFSleaders(edgeList, ftimes, headAlias, source, explored, leaders)

def kosaraju(edgeList):

  explored = set()
  ftimes = dict()
  t = 0
  verticeSet = set()

  for (tail, head) in edgeList:
    verticeSet.add(head)
    verticeSet.add(tail)

  for vertex in range(max(verticeSet), min(verticeSet)-1, -1): 
    if vertex not in explored:
      t = DFSftimes(edgeList, vertex, explored, ftimes, t)

  explored = set()
  leaders = dict()

  for vertex in range(t, 0, -1):
    if vertex not in explored:
      DFSleaders(edgeList, ftimes, vertex, vertex, explored, leaders)

  return leaders

if __name__ == '__main__':

  filename = sys.argv[1]
  edgeList = createEdgeList(filename)

