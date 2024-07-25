from collections import Counter

S = input()

count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
count.update(Counter(S))

print(' '.join(str(count[chr(i)]) for i in range(ord('a'), ord('z') + 1)))
