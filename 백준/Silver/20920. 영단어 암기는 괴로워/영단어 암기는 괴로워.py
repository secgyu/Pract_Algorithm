import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

filtered_words = [word for word in words if len(word) >= M]
word_count = Counter(filtered_words)

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)
