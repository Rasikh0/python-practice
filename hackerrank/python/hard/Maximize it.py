K, M = list(map(int, input().split()))

lists = [list(map(int, input().split()))[1:] for _ in range(K)]

possible_sums = {0}

for lst in lists:
    new_sum = set()
    for num in lst:
        for s in possible_sums:
            new_sum.add((s + num**2)%M)
    
    possible_sums = new_sum

print(max(possible_sums))
