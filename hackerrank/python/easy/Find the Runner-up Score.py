if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    def runnerup(arr,n):
        arr = set(arr)
        arr = sorted(arr)
        runnerup_score = arr[-2]
        print(runnerup_score)
        
    runnerup(arr,n)
