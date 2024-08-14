import sys
input = sys.stdin.readline

def merge_sort(s, e):
    if (s < e):
        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m+1, e)
        merge(s, m, e)

def merge(s, m, e):
    i, j, t = s, m+1, 0

    while i <= m and j <= e:
        if A[i] <= A[j]:
            result.append(A[i])
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            result.append(A[j])
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= m:
        result.append(A[i])
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= e:
        result.append(A[j])
        tmp[t] = A[j]
        t += 1
        j += 1
    i = s
    t = 0
    while i <= e:
        A[i] = tmp[t]
        i += 1
        t += 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = list(0 for _ in range(N))
result = list()

merge_sort(0, N-1)

if K <= len(result):
    print(result[K-1])
else:
    print(-1)