import re
t = int(input())

for _ in range(t):
    s = input().strip()
    pattern = r"^[+-]?[0-9]*\.[0-9]+$"
    print(bool(re.match(pattern, s)))
