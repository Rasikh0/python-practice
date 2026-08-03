import re
import email.utils

n = int(input())

for _ in range(n):
    emls = email.utils.parseaddr(input())
    em = re.match(r"^[A-Za-z](\w|-|\.){1,}@([A-Za-z]{1,})\.[A-Za-z]{1,3}$", emls[1])
    if(em):
        print(email.utils.formataddr(emls))
