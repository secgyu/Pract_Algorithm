MOD = 1_000_000_007

def mod_inverse(b, mod):
    result = 1
    exp = mod - 2
    while exp > 0:
        if exp % 2:  
            result = (result * b) % mod
        b = (b * b) % mod  
        exp //= 2  
    return result

def expected_value_sum(dice_list, mod):
    total = 0
    for n, s in dice_list:
        inv_n = mod_inverse(n, mod) 
        total = (total + s * inv_n) % mod
    return total

M = int(input()) 
dice_list = [tuple(map(int, input().split())) for _ in range(M)]

print(expected_value_sum(dice_list, MOD))
