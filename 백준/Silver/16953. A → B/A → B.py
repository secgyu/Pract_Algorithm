def min_operations(A, B):
    count = 1
    while B > A:
        if B % 2 == 0:
            B //= 2
        elif B % 10 == 1:  
            B //= 10
        else:
            return -1
        count += 1
    return count if B == A else -1

A, B = map(int, input().split())
print(min_operations(A, B))
