from itertools import * # * means import all, groupby() will be included

n = input()

for i, j in groupby(n):
    print(tuple([len(list(j)), int(i)]), end=" ")
