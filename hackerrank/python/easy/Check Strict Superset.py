l = set(map(int, input().split()))
n = int(input())
val = ""

for _ in range(n):
    l1 = set(map(int, input().split()))
    if len(l1.difference(l)) == 0:
        val = "True"
    else:
        val = "False"
        break
print(val)
