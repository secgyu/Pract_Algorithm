import math
N = int(input())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0


def isPalindrom(target):
    tmp = list(str(target))

    start = 0
    end = len(tmp)-1

    while (start < end):
        if tmp[start] != tmp[end]:
            return False
        start += 1
        end -= 1
    return True


i = N
while True:
    if A[i] != 0:
        result = A[i]
        if (isPalindrom(result)):
            print(result)
            break
    i += 1
