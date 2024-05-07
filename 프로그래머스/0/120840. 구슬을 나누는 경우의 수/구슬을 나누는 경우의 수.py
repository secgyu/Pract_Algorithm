import math
def solution(balls, share):
    mo1 = math.factorial(balls - share)
    mo2 = math.factorial(share)
    ja = math.factorial(balls)
    answer = ja / (mo1 * mo2)
    return answer