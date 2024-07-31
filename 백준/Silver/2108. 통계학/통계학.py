import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input().strip()))

mean = round(sum(numbers) / N)

numbers.sort()
median = numbers[N // 2]

count = Counter(numbers)
mode_freq = count.most_common()
modes = [k for k, v in mode_freq if v == mode_freq[0][1]]

if len(modes) > 1:
    mode = sorted(modes)[1]
else:
    mode = modes[0]

range_val = max(numbers) - min(numbers)


print(mean)
print(median)
print(mode)
print(range_val)
