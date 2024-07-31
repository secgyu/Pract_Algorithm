import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    VPS = list(input().rstrip())
    sum = 0
    answer = 'YES'

    for i in range(len(VPS)):
        if VPS[i] == '(':
            sum += 1
        else:
            sum -= 1
            if sum < 0:
                answer = 'NO'

    if sum > 0:
        answer = 'NO'
    elif sum < 0:
        answer = 'NO'
    print(answer)
