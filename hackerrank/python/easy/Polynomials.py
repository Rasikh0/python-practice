import numpy

arr = numpy.array(input().split(), dtype=float)

print(numpy.polyval(arr, int(input())))
