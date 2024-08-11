a, b = map(int, input().split())
seq = []

num = 1
while len(seq) < b:
    seq.extend([num] * num)
    num += 1
print(sum(seq[a-1:b]))