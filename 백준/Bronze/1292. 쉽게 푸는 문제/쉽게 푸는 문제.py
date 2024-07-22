start, end = map(int, input().split())

seq = []
n = 1

while len(seq) < end:
    seq.extend([n] * n)
    n += 1

result = sum(seq[start-1:end])
print(result)
