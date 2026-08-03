import re

N = int(input())

for _ in range(N):
    inp = input()
    if(bool(re.search(r"^#", inp)) == False):
        t = re.findall(r"#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}", inp)
        if(t!=[]):
            print(*t, sep="\n")
