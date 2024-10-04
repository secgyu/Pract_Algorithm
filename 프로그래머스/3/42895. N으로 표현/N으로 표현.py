def solution(N, number):
    # dp[i]는 N을 i번 사용해서 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) # n, nn, nnn

    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)

                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i
    return -1

print(solution(5, 12))