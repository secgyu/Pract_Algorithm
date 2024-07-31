case = int(input())

result = []

for _ in range(case):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]

    average = sum(scores) / N

    average_count = sum(1 for score in scores if score > average)

    percent = (average_count / N) * 100

    result.append(f"{percent:.3f}%")

for i in result:
    print(i)
