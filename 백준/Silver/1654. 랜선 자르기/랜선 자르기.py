import sys

k, n = map(int, sys.stdin.readline().split())  
lines = [int(sys.stdin.readline()) for _ in range(k)] 
start = 1 
end = max(lines)
result = 0  

while start <= end:
    mid = (start + end) // 2 
    count = sum(line // mid for line in lines) 
    if count >= n: 
        result = mid  
        start = mid + 1  
    else: 
        end = mid - 1
print(result)
