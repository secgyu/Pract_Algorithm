import math

def solution(progresses, speeds):
    answer = []
    days = [] # 7,3,9

    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress # 남은 기능개발
        day = math.ceil(remain / speed)
        days.append(day)
    
    distribution_day = days[0] # 시작 배포날짜 
    count = 1

    for i in range(1, len(days)):
        if days[i] <= distribution_day: # 3 < 7 count2 9
            count += 1
        else :
            answer.append(count)
            distribution_day = days[i]
            count = 1
    answer.append(count)
    return answer