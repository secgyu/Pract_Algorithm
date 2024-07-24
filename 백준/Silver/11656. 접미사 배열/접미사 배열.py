S = input()
seq = []

for i in range(len(S)):
    seq.append(S[i:])

seq.sort()

for i in seq:
    print(i)
