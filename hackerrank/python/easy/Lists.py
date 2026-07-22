if __name__ == '__main__':
    N = int(input())
    
    arr = []
    for n in range(N):
        line = input()
        pieces = line.split()
        if pieces[0] == "insert":arr.insert(int(pieces[1]), int(pieces[2]))
        elif pieces[0] == "print": print(arr)
        elif pieces[0] == "remove": arr.remove(int(pieces[1]))
        elif pieces[0] == "append": arr.append(int(pieces[1]))
        elif pieces[0] == "sort": arr.sort()
        elif pieces[0] == "pop": arr.pop()
        elif pieces[0] == "reverse": arr.reverse()
