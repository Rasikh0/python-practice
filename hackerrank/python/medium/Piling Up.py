def can_stack_cubes(blocks):
    left = 0
    right = len(blocks) - 1
    current_top = float('inf')
    
    while left <= right:
        if blocks[left] >= blocks[right]:
            chosen_cube = blocks[left]
            left += 1
        else:
            chosen_cube = blocks[right]
            right -= 1
        
        if chosen_cube > current_top:
            return "No"
        
        current_top = chosen_cube
    return "Yes"

T = int(input())
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(can_stack_cubes(blocks))
