import sys
input = sys.stdin.readline


def sieve(max_num):
    is_prime = [True] * (max_num+1)
    is_prime[0], is_prime[1] = False, False

    num = 2
    while num * num <= max_num:
        if is_prime[num]:
            for i in range(num * 2, max_num + 1, num):
                is_prime[i] = False

        num += 1
    return is_prime


max_num = 123456 * 2
sieve_seq = sieve(max_num)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0

    for num in range(n+1, 2*n+1):
        if sieve_seq[num]:
            count += 1
    print(count)
