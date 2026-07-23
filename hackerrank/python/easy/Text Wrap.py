import textwrap

def wrap(string, max_width):
    output = textwrap.fill(string, max_width)
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
