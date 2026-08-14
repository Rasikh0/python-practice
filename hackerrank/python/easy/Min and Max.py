import numpy

n, m = list(map(int, input().split()))
arr = numpy.array([input().split() for i in range(n)], dtype=int)

minAxis = numpy.min(arr, axis=1)
print(max(minAxis))
