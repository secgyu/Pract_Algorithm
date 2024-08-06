total_price = int(input())

sum_known_prices = 0

for _ in range(9):
    price = int(input())
    sum_known_prices += price

unreadable_book_price = total_price - sum_known_prices

print(unreadable_book_price)
