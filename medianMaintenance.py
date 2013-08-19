import sys
import heapq

def medianMaintenance(numList):
  """
  Input: list of numbers
  Output: list of temporary medians at successive insertions of numbers from input list. 
  After processing the whole input list, the last element of output list will be equal to
  the median of all numbers from input list
  """


  # initialize low-values (lower or equal to median) heap and high-values
  # (higher than median) heap
  # lowHeap simulates extract-max by negating elements, highHeap supports extract-min
  lowHeap = []
  highHeap = []

  currentMedian = float('inf')
  i = 1
  medianList = []

  for num in numList:
    if i == 1:
      heapq.heappush(lowHeap, -num)
      currentMedian = num
      medianList.append(currentMedian)
      i += 1
      continue 
    elif num <= currentMedian:
      if i-1 % 2 != 0:
        heapq.heappush(highHeap, currentMedian)
        heapq.heappop(lowHeap)
      heapq.heappush(lowHeap, -num)
    elif num > currentMedian:
      if i-1 % 2 == 0:
        highElem = heapq.heappop(highHeap)
        heapq.heappush(lowHeap, -highElem)
      heapq.heappush(highHeap, num)
    if i%2 == 0:
      currentMedian = (-lowHeap[0] + highHeap[0])/2
    else:
      currentMedian = -lowHeap[0]

    medianList.append(currentMedian)
    i += 1

  return medianList

if __name__ == '__main__':
  filename = sys.argv[1]
  f = open(filename)
  numList = [ int(line) for line in f ]
  medianList = medianMaintenance(numList)
  print(medianList)
