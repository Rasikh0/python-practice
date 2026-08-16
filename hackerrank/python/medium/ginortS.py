# Enter your code here. Read input from STDIN. Print output to STDOUT

user_input = input().strip()

sorted_string = ''.join(sorted(
    user_input,
    key=lambda x: (
        x.isdigit() and int(x) % 2 == 0,
        x.isdigit() and int(x) % 2 != 0,
        x.isupper(),
        x
    )
))

print(sorted_string)
