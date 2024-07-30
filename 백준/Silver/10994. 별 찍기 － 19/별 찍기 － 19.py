def draw_star(n):
    size = 4 * n - 3
    canvas = [[' ' for _ in range(size)] for _ in range(size)]

    def fill_square(x, y, n):
        if n == 1:
            canvas[x][y] = '*'
            return
        length = 4 * n - 3
        for i in range(length):
            canvas[x][y + i] = '*'
            canvas[x + length - 1][y + i] = '*'
            canvas[x + i][y] = '*'
            canvas[x + i][y + length - 1] = '*'
        fill_square(x + 2, y + 2, n - 1)

    fill_square(0, 0, n)

    for row in canvas:
        print(''.join(row))


n = int(input())
draw_star(n)
