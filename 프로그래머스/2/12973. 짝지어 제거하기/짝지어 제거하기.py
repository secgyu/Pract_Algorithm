def solution(s):
    stack = []  # 문자열의 각 문자를 담을 스택
    
    # 주어진 문자열을 하나씩 순회하면서 짝을 이루는 문자 제거
    for i in s:
        # 1. 스택이 비어있으면 문자를 스택에 추가
        if len(stack) == 0:
            stack.append(i)
        # 2. 스택의 맨 위에 있는 문자와 현재 문자가 같으면 (짝이 맞으면) 제거
        elif stack[-1] == i:
            stack.pop()
        # 3. 스택의 맨 위에 있는 문자와 현재 문자가 다르면 스택에 추가
        else:
            stack.append(i)
    
    # 4. 모든 문자를 처리한 후 스택이 비어있으면 짝이 맞는 모든 문자가 제거된 것
    if len(stack) == 0:
        return 1  # 모든 짝이 제거되었으므로 성공적으로 처리
    else:
        return 0  # 스택에 남아있다면 짝이 남아있으므로 처리 실패
