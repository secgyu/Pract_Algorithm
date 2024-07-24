import sys
input = sys.stdin.readline


# n!, m!, (n-m)!

n, m = map(int, input().split())


def factor(n, factor):
    count = 0

    while n >= factor:
        n = n // factor
        count = count + n
    return count


# n!
count_2_n = factor(n, 2)
count_5_n = factor(n, 5)

# m!
count_2_m = factor(m, 2)
count_5_m = factor(m, 5)

# (n-m)!
count_2_nm = factor(n-m, 2)
count_5_nm = factor(n-m, 5)

# nCm
count_final2 = count_2_n - (count_2_m + count_2_nm)
count_final5 = count_5_n - (count_5_m + count_5_nm)

result = min(count_final2, count_final5)

print(result)