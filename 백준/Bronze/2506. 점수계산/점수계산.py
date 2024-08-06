N = int(input())

results = list(map(int, input().split()))

total_score = 0
current_streak = 0

for result in results:
    if result == 1:
        current_streak += 1
        total_score += current_streak
    else:
        current_streak = 0

print(total_score)
