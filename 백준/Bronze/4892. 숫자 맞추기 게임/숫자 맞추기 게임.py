import sys
input = sys.stdin.read

data = input().split()
case_number = 1

for n0 in data:
    n0 = int(n0)
    if n0 == 0:
        break

    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 // 2
        parity = "even"
    else:
        n2 = (n1 + 1) // 2
        parity = "odd"
    
    n3 = 3 * n2
    n4 = n3 // 9

    print(f"{case_number}. {parity} {n4}")
    case_number += 1