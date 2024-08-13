N = int(input())
seq = list(map(int, input().split()))
S = [0] * N
seq.sort()

S[0] = seq[0]

for i in range(1, N):
    S[i] = S[i-1] + seq[i]

sum = 0

for i in range(0, N):
    sum += S[i]
print(sum)