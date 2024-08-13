octal_num = input()

decimal_number = int(octal_num, 8)
binary_number = bin(decimal_number)[2:]
print(binary_number)