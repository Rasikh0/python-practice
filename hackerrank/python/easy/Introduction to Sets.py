def average(array):
    distinct_heights = set(arr)
    average_height = sum(distinct_heights)/len(distinct_heights)
    
    return round(average_height, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
