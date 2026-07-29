from itertools import combinations_with_replacement

string, k = input().split()
k = int(k)

for item in list(combinations_with_replacement(sorted(string), k)):
    print(''.join(item))
