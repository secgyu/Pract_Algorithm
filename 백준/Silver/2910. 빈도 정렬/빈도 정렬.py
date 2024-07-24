from collections import Counter
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
seq = list(map(int, input().split()))

freq = Counter(seq)
first_apperance = {}

for idx, num in enumerate(seq):
    if num not in first_apperance:
        first_apperance[num] = idx

sort_seq = freq.most_common()
print(" ".join(map(lambda x: ' '.join([str(x[0])] * x[1]), sort_seq)))
