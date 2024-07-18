m, n = map(int, input().split())
board = []

for _ in range(m):
    board.append(list(input()))

color = {0: 'B', 1: 'W'}
paint = 10**9
for x_start in range(m-7):
    for y_start in range(n-7):
        paint_b, paint_w = 0, 0
        for x in range(x_start, x_start+8):
            for y in range(y_start, y_start+8):
                if board[x][y] != color[(x-x_start+y-y_start) % 2]:
                    paint_b += 1
                else:
                    paint_w += 1
        paint = min(paint, paint_b, paint_w)
print(paint)
