def count_substring(string, sub_string):
    count = 0
    for n in range(len(string)):
        if string[n:n+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
