size, where = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
print(seq[where - 1])
