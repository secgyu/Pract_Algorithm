A = int(input())
B = int(input())
C = int(input())

product = A * B * C

product_str = str(product)

seq = [0] * 10

for num in product_str:
    seq[int(num)] += 1

for i in seq:
    print(i)
