import sys
n=int(sys.stdin.readline())
tmp=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in range(n):
    for j in range(n):
        cnt+=abs(tmp[i]-tmp[j])
print(cnt)
