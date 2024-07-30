def check_line(x1, y1, x2, y2, x3, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return "WHERE IS MY CHICKEN?"
    else:
        return "WINNER WINNER CHICKEN DINNER!"


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(check_line(x1, y1, x2, y2, x3, y3))
