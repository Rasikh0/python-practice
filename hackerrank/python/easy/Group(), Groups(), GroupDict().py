#work on writing regex expressions

import re

s = input().strip()

pattern = r"([A-Za-z0-9])\1" # \1 means whatever value you have on the other side of \ you want it on the right too. So, repetition of two values back to back like 22, 11. 

m = re.search(pattern, s)

if m:
    print(m.group(1)) #group 1 prints the number like 1 here. group 0 print the repetition 11.
else:
    print(-1)
