N = int(input())
seq = set(map(int, input().split()))
sort_seq = sorted(seq)
print(' '.join(map(str, sort_seq)))