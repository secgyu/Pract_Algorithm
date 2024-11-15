import math
import sys
input = sys.stdin.readline

def total_comb(n, m):
    return math.factorial(n + m) // (math.factorial(n) * math.factorial(m))

def search(n, m, k):
    if total_comb(n, m) < k:
        return -1

    result = []
    while n > 0 and m > 0:
        a_count = total_comb(n - 1, m)  # a 먼저 했을 때, 조합
        if k <= a_count:
            result.append('a')
            n -= 1
        else:
            result.append('z')
            k -= a_count
            m -= 1

    # 남는 a와 z 추가
    result.extend(['a'] * n)
    result.extend(['z'] * m)
    return ''.join(result)

n, m, k = map(int, input().split())
final_result = search(n, m, k)
print(final_result)
