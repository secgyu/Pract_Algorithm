T = int(input())

for _ in range(T):
    yonsei_score = 0
    korea_score = 0

    for _ in range(9):
        y, k = map(int, input().split())
        yonsei_score += y
        korea_score += k

    if yonsei_score > korea_score:
        print("Yonsei")
    elif korea_score > yonsei_score:
        print("Korea")
    else:
        print("Draw")
