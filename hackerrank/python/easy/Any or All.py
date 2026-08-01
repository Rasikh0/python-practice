n = int(input())
numbers = list(map(int, input().split()))

# condition1 & condition2:
print(all(x > 0 for x in numbers) & any(str(x) == str(x)[::-1] for x in numbers))
