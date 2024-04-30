def solution(n, k):
    sheep_price = 12000
    drink_price = 2000
    total_sheep_price = n * sheep_price
    free_drink = n // 10
    total_drink_price = (k - free_drink) * drink_price
    
    answer = total_sheep_price + total_drink_price
    return answer