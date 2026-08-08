n, m = list(map(int, input().split()))
my_array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

def calculate_happiness(n, m, my_array, set_a, set_b):
    happiness = 0
    
    for num in my_array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    
    return happiness

print(calculate_happiness(n, m, my_array, set_a, set_b))
