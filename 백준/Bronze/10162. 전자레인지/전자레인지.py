T = int(input())

A = 300  
B = 60   
C = 10   

a_count = 0
b_count = 0
c_count = 0

a_count = T // A
T %= A

b_count = T // B
T %= B

c_count = T // C
T %= C

if T != 0:
    print(-1)
else:
    print(a_count, b_count, c_count)
