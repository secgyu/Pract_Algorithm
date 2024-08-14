import sys
input = lambda:sys.stdin.readline().rstrip()

left = list(input())
right = []

M = int(input())

for _ in range(M):
    cmd = list(input().split())

    if cmd[0] == 'L' and left:
        right.append(left.pop())
    
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    
    elif cmd[0] == 'B' and left:
        left.pop()
    
    elif cmd[0] == 'P':
        left.append(cmd[1])

result = left + right[::-1]
print(''.join(result))