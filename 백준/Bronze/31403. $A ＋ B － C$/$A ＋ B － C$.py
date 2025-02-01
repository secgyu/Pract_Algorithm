import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()
num_result = int(A) + int(B) - int(C)
str_result = str(int(A + B) - int(C))

print(num_result)
print(str_result)
