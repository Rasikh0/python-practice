from itertools import combinations

string, k = input().split()
k = int(k)

for i in range(1, k+1):
    for j in combinations(sorted(string), i):
        print(''.join(j))
