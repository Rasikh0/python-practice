cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_sequence = [0,1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    return fib_sequence[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
