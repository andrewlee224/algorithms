import sys

def get2sumcount(filename):
  f = open(filename)
  intArray = [ int(line) for line in f ]
  count2sum = 0
  intSet = set(intArray)
  intArray = list(intArray)

  for t in range(-10000,10001):
    for num in intSet:
      if t-num in intSet:
        count2sum += 1
        break
    progress = (t+10001)*100/20001
    sys.stdout.write("Progress: %f%%  \r" % (progress) )
    sys.stdout.flush()

  return count2sum
  
if __name__ == '__main__':
  print(get2sumcount(sys.argv[1]))
