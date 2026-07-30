students_eng = int(input())
subscribers_eng = set(map(int, input().split()))
students_fren = int(input())
subscribers_fren = set(map(int, input().split()))

answer = subscribers_eng.symmetric_difference(subscribers_fren)

print(len(answer))
