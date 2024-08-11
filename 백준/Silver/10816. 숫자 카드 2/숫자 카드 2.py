import sys
input = sys.stdin.readline

N = int(input())
N_card = list(map(int, input().split()))
M  = int(input())
M_card = list(map(int, input().split()))

dict = {}

for i in N_card:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for num in M_card:
    if num in dict:
        print(dict[num], end= ' ')
    else:
        print(0, end=' ')