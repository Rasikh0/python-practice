from itertools import combinations

n = int(input())
list_letters = input().split()
k = int(input())

comb_items = list(combinations(list_letters, k))

count = 0
for comb in comb_items:
    if 'a' in comb:
        count += 1

probability_of_a = count / len(comb_items)
print(f"{probability_of_a: .3f}")
