T = int(input())

for _ in range(T):
    N = int(input())

    print('#' * N)

    for i in range(N - 2):
        print('#' + 'J' * (N-2) + '#')
    
    if N > 1:
        print('#' * N)
    
    if _ < T-1:
        print()