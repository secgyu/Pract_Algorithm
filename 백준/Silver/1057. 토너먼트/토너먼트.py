N, jimin, hansu = map(int, input().split())

round_number = 1

while True:
    jimin = (jimin + 1) // 2
    hansu = (hansu + 1) // 2

    if jimin == hansu:
        break
    round_number += 1
print(round_number)