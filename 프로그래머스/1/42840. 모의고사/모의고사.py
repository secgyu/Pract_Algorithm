def solution(answer):
    human1 = [1, 2, 3, 4, 5]
    human2 = [2, 1, 2, 3, 2, 4, 2, 5]
    human3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1, count2, count3 = 0, 0, 0

    for i in range(len(answer)):
        if human1[i % len(human1)] == answer[i]:
            count1 += 1
        if human2[i % len(human2)] == answer[i]:
            count2 += 1
        if human3[i % len(human3)] == answer[i]:
            count3 += 1
    
    correct = max(count1, count2, count3)
    answer = []

    if correct == count1:
        answer.append(1)

    if correct == count2:
        answer.append(2)

    if correct == count3:
        answer.append(3)

    return answer