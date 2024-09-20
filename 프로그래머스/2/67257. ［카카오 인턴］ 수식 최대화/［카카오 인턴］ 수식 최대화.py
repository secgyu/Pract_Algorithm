from itertools import permutations

def solution(expression):
    answer = 0
    operators = ['+', '-', '*']
    operator_permutation = list(permutations(operators, 3))
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.replace('*', ' * ')
    expression = expression.split()
    
    for operator in operator_permutation:
        temp_expression = expression.copy() # 깊은 복사하는 이유는 expression을 수정하면 안되기 때문 왜냐하면 다음 연산자 순열을 위해 원본이 필요하기 때문
        for op in operator:
            while op in temp_expression:
                idx = temp_expression.index(op) # 연산자의 인덱스 찾기
                temp_expression[idx-1] = str(eval(temp_expression[idx-1] + op + temp_expression[idx+1])) 
                # 연산자 앞의 숫자와 뒤의 숫자를 연산자로 계산한 결과를 
                # 연산자 앞의 숫자에 저장 예를들어 1+2*3 이면 1+6 이렇게 저장
                temp_expression.pop(idx+1) # 연산자 뒤의 숫자 삭제
                temp_expression.pop(idx) # 연산자 삭제 
                #삭제한 연산자와 연산자 뒤의 숫자를 삭제했기 때문에 연산자 앞의 숫자만 남음
                # 삭제한 이유는 연산자를 계산했기 때문에 필요가 없어졌기 때문
        answer = max(answer, abs(int(temp_expression[0]))) # 0번째 인덱스에는 연산자가 없는 숫자만 남아있기 때문에 절대값을 취한후 최대값을 찾음
    return answer