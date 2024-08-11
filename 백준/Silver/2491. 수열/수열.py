def find_longest_subsequence(n, sequence):
    if n == 1:
        return 1

    increase_len = 1
    decrease_len = 1
    max_len = 1

    for i in range(1, n):
        if sequence[i] > sequence[i - 1]:
            increase_len += 1
            decrease_len = 1
        elif sequence[i] < sequence[i - 1]:
            decrease_len += 1
            increase_len = 1
        else:
            increase_len += 1
            decrease_len += 1
        
        max_len = max(max_len, increase_len, decrease_len)

    return max_len

n = int(input())
sequence = list(map(int, input().split()))

print(find_longest_subsequence(n, sequence))
