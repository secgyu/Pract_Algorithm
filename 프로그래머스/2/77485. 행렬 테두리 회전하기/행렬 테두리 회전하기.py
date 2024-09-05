def solution(rows, columns, queries):
    answer = []
    grid = []

    #행렬 만들기
    for row in range(rows):
        grid.append([num for num in range(row*columns+1, (row+1)*columns+1)])
    
    #테두리 회전(이동)
    for query in queries:
        query = [x-1 for x in query] #0부터 시작해서
        temp = grid[query[0]][query[1]] #왼쪽대각선 제일 위 값
        small = temp

        r1, c1, r2, c2 = query

        #왼쪽
        for i in range(r1+1, r2+1):
            grid[i-1][c1] = grid[i][c1]
            small = min(small, grid[i-1][c1])
        #아래 -> 26 26 나와서 먼저함
        for i in range(c1+1, c2+1):
            grid[r2][i-1] = grid[r2][i]
            small = min(small, grid[r2][i-1])
        #오른쪽 -> 28 28 나와서
        for i in range(r1+1, r2+1)[::-1]:
            grid[i][c2] = grid[i-1][c2]
            small = min(small, grid[i][c2])
        #위쪽
        for i in range(c1+1, c2+1)[::-1]:
            grid[r1][i] = grid[r1][i-1]
            small = min(small, grid[r1][i])
        grid[r1][c1+1] = temp

        answer.append(small)

    return answer