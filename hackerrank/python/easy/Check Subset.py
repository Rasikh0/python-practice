t = int(input())

for _ in range(t):
    elements_A = int(input())
    set_A = set(map(int, input().split()))
    elements_B = int(input())
    set_B = set(map(int, input().split()))

    print(set_A.issubset(set_B))
