import sys

# MergeSort algorithm implementation
# Running time O(n*log(n))
# Accepts a newline delimited list of integers and prints out the sorted
# list to console.
# Usage: mergeSort.py <filename>
# By Andrew Lichaczewski

def mergeSort(A): 
  length = len(A)
  if (length <= 1): return A

  halfLength = length//2 if (length%2 == 0) else (length+1)//2
  B = mergeSort(A[:halfLength])
  C = mergeSort(A[halfLength:])

  D = []
  i, j = 0, 0

  for k in range(length):
    if (i == len(B) or j == len(C)): break

    if (B[i] < C[j]):
      D.append(B[i])
      i = i+1
    else:
      D.append(C[j])
      j = j+1

  while(i < len(B)):
    D.append(B[i])
    i = i+1

  while(j < len(C)):
    D.append(C[j])
    j = j+1

  return D

if __name__ == '__main__':

  filename = sys.argv[1]
  file = open(filename)

  numbers = [int(line.strip()) for line in file]
  sortedNumbers = mergeSort(numbers)

  print(sortedNumbers)
