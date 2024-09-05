def solution(s):
    answer = []  # 최종 결과를 담을 리스트
    
    # 1. 문자열에서 앞뒤의 중괄호 '{}'를 제거한 후, 내부의 각 부분집합을 ','를 기준으로 나눠줍니다.
    #    예: "{{20,111},{111}}" -> "20,111},{111"
    s = s.lstrip('{').rstrip('}').split('},{')
    
    # 2. 각 부분집합을 정수로 변환하고, 이를 set으로 묶어줍니다.
    #    예: ['20,111', '111'] -> [{20, 111}, {111}]
    s = [set(map(int, x.split(','))) for x in s]
    
    # 3. 각 집합의 길이를 기준으로 오름차순으로 정렬합니다.
    #    예: [{111}, {20, 111}]
    s.sort(key=len)
    
    # 4. 이전 단계에서 처리한 집합을 저장할 변수. 초기값은 빈 집합.
    prev_set = set()

    # 5. 각 단계에서 새로운 숫자를 찾아내어 answer에 추가하는 작업
    for current_set in s:
        # 현재 집합(current_set)에서 이전 집합(prev_set)을 뺀 차집합을 구합니다.
        # 차집합에는 새로운 숫자가 1개만 남으므로, 이를 리스트로 변환 후 첫 번째 요소를 추출합니다.
        new_element = list(current_set - prev_set)[0]
        
        # 6. 새로 발견한 요소를 정답 리스트에 추가합니다.
        answer.append(new_element)
        
        # 7. 현재 집합을 prev_set에 저장하여, 다음 반복에서 사용합니다.
        prev_set = current_set
    
    # 8. 모든 작업을 마치고 완성된 answer 리스트를 반환합니다.
    return answer