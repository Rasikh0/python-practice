# input() is only for python2. The code below runs in python3. 

x, k = list(map(int, input().split()))
s = input()
print(eval(s) == k)
    
