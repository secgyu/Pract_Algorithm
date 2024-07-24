import math
N = int(input())
A = [0] * (2000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0


def isPalindrom(target):
    tmp = str(target)
    return tmp == tmp[::-1]


for i in range(N, len(A)):
    if A[i] != 0 and (isPalindrom(A[i])):
        print(A[i])
        break
