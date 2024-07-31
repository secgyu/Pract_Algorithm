N = int(input())
student = list(map(int, input().split()))

stack = []
answer = 'Nice'
turn = 1

for i in student:
    stack.append(i)

    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if stack:
    print('Sad')
else:
    print('Nice')
