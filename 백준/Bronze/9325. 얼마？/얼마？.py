T = int(input())

for _ in range(T):
    base_price = int(input())
    
    n = int(input())
    
    total_price = base_price
    
    for _ in range(n):
        q, p = map(int, input().split())
        total_price += q * p
    
    print(total_price)
