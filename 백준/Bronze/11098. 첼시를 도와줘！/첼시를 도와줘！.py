n = int(input())

for _ in range(n):
    p = int(input())
    
    max_price = -1
    max_price_player = ""
    
    for _ in range(p):
        price, name = input().split(maxsplit=1)
        price = int(price)
        
        if price > max_price:
            max_price = price
            max_price_player = name
    
    print(max_price_player)
