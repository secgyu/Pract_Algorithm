N = int(input())
gomgomi = set()
count = 0

for _ in range(N):
    user = input()
    if user == 'ENTER':
        count += len(gomgomi)
        gomgomi = set()
    
    else :
        gomgomi.add(user)
count += len(gomgomi)
print(count)