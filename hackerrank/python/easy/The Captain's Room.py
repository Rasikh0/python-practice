from collections import Counter

k = int(input())
room_list = list(map(int, input().split()))

room_counts = Counter(room_list)

for room_number, room_count in room_counts.items():
    if room_count == 1:
        print(room_number)
