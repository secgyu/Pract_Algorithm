m=int(input())
n=int(input())
arr=[]
tmp=0

for i in range(1,100+1):
    if m<=i**2 and i**2<=n:
        tmp+=i**2
        arr.append(i**2)

if tmp==0 and len(arr)==0:
    print(-1)
else:
    print(tmp)
    print(arr[0])