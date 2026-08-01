import re

s = input()
vowels = '[aeiouAEIOU]'
consonants = '[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]'

match = re.findall((r'(?<={c})({v}{{2,}})(?={c})'.format(c = consonants, v = vowels)), s)

if match == []:
    print(-1)
else:
    for i in match:
        print(i)
