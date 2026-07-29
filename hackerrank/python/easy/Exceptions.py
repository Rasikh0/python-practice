T = int(input())

for i in range(T):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
