from itertools import permutations
import math

def check_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    seq = []

    for i in range(1, len(numbers) + 1):
        seq += (permutations(numbers, i))
    
    
    finish_num = [int(''.join(seqs)) for seqs in seq]
    answer = []

    for i in finish_num:
        if check_prime(i):
            answer.append(i)
    
    return len(set(answer))