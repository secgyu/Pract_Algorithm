from collections import defaultdict
from bisect import bisect_left, bisect_right

def make_combination(info):
    conditions = info[:-1] # 마지막 점수 빼고 조건만 저장
    score = int(info[-1]) # 점수 저장
    all_combinations = [] # 모든 조합을 저장할 리스트

    for i in range(16):
        temp_comb = [] # 새로운 조합을 저장할 리스트 (임시)
        for j in range(4): # 4개의 조건에 대해
            if i & (1 << j): # i의 j번째 비트가 1이면
                temp_comb.append('-') # -를 추가
            else:
                temp_comb.append(conditions[j]) # 아니면 조건을 추가
        all_combinations.append((temp_comb, score)) # 조합과 점수를 튜플로 저장
    return all_combinations

# defaultdict는 딕셔너리 기본값 설정을 위해 사용

def solution(infos, query):
    info_dict = defaultdict(list) # 조건과 점수를 저장할 딕셔너리 

    for info in infos:
        info = info.split()
        combs = make_combination(info) # 조건과 점수를 만들어주는 함수
        for comb, score in combs:
            info_dict[''.join(comb)].append(score)
    
    # 이진탐색 위해서 정렬
    for key in info_dict:
        info_dict[key].sort()
    
    answer = []

    for q in query:
        query = q.replace(' and ', ' ').split()
        condition = ''.join(query[:-1]) 
        score_threshold = int(query[-1])

        if condition in info_dict:
           scores = info_dict[condition]
           idx = bisect_left(scores, score_threshold)
           answer.append(len(scores) - idx)
        else:
            answer.append(0)
        
    return answer