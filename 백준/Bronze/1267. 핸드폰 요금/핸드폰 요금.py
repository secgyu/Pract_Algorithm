import math
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])  
times = list(map(int, data[1:N+1])) 

Y = 0  
M = 0  

for time in times:
    Y += ((time // 30) + 1) * 10
    M += ((time // 60) + 1) * 15

if Y < M:
    print(f"Y {Y}")
elif M < Y:
    print(f"M {M}")
else:
    print(f"Y M {Y}")
