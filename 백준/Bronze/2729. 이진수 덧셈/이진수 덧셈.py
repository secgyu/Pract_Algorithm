T = int(input())

for _ in range(T):
    sum = 0
    binary1, binary2 = input().split()
    num1 = int(binary1, 2)
    num2 = int(binary2, 2)
    sum = num1 + num2

    binary_sum = bin(sum)[2:]

    print(binary_sum)