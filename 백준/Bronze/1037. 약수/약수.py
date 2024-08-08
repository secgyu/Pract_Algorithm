num_of_divisors = int(input())
divisors = list(map(int, input().split()))

N = min(divisors) * max(divisors)

print(N)
