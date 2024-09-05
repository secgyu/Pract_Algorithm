def solution(n):
    grid = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    number = 1
    for i in range(n):
        for _ in range(i, n):

            if i % 3 == 0: 
                x += 1

            elif i % 3 == 1:
                y += 1
            
            elif i % 3 == 2:
                x -= 1
                y -= 1

            grid[x][y] = number
            number += 1
    
    for i in range(n):
        answer += grid[i][:i+1]
    return answer