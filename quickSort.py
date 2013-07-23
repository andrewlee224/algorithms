import sys

def quickSort(A, l, r):
  # print("l: " + str(l) + ", r: " + str(r))
  if (r - l <= 0): return 0

  pivot = A[l]
  j = l + 1

  for i in range(l + 1, r + 1):
    # print("i: " + str(i))
    # print("j: " + str(j))
    if (A[i] < pivot):
      # print("A[i] < pivot")
      if (i != j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
      j = j+1
      # print("j: " + str(j))

  temp = A[j-1]
  A[j-1] = pivot
  A[l] = temp

  c1 = quickSort(A, l, j-2)
  c2 = quickSort(A, j, r)

  return c1 + c2 + (r - l)



filename = sys.argv[1]
file = open(filename)

nums = [int(line.strip()) for line in file]

comparisons = quickSort(nums, 0, len(nums) - 1)
print(nums[100:120])
print("Number of comparisons: " + str(comparisons))
