n, x = list(map(int, input().split()))
marks = []

for _ in range(x):
    course = list(map(float, input().split()))
    marks.append(course)

for student_marks in list(zip(*marks)):
    print(sum(student_marks)/x)
