import sys

def sortAndCount(A):

  length = len(A)

  if length == 1:
    return (A, 0)
  
  if (length % 2 == 0):
    halfLength = length//2
  else:
    halfLength = (length-1)//2 + 1

  B, x = sortAndCount(A[:halfLength])
  C, y = sortAndCount(A[halfLength:])
  D, z = mergeAndCount(B, C)
  
  return (D, x+y+z)

def mergeAndCount(B, C): 
  i, j, count = 0, 0, 0
  D = []
  
  for k in range(len(B) + len(C)):
    if (i == len(B) or j == len(C)): break
    if (i < len(B) and B[i] < C[j]): 
        D.append(B[i])
        i = i+1
    else: 
      if (j < len(C)):
        D.append(C[j])
        j = j+1 
        count = count + (len(B) - i)

  while (i < len(B)):
    D.append(B[i])
    i = i+1

  while (j < len(C)):
    D.append(C[j])
    j = j+1

  return (D, count) 

filename = sys.argv[1]
file = open(filename)

numbers = [int(line.strip()) for line in file]
sortedNumbers, invCount = sortAndCount(numbers)


# print(numbers)
print(invCount)
