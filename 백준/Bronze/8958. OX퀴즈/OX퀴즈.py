import sys
input = sys.stdin.read

data = input().split()

test_cases = int(data[0])

results = []

for i in range(1, test_cases + 1):
    case = data[i]
    score = 0
    current_streak = 0
    for char in case:
        if char == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0
    results.append(score)

for result in results:
    print(result)
