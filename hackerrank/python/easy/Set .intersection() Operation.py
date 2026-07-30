n_English = int(input())
english_subscribers = set(map(int, input().split()))
n_french = int(input())
french_subscribers = set(map(int, input().split()))

answer = english_subscribers.union(french_subscribers)

print(len(answer))
