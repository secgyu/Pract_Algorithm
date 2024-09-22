from collections import deque

def solution(price):
    answer = []
    queue = deque(price) #[1,2,3,2,3]

    while queue:
        current_price = queue.popleft() #[1] [2,3,2,3] 
        count = 0

        for price in queue:
            count += 1

            if price < current_price:
                break
        answer.append(count)
    return answer