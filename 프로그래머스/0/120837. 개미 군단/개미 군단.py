def solution(hp):
    answer = 0
    General_Attack = 5
    Soldier_Attack = 3
    Work_Attack = 1
    
    while(hp > 0):
        if hp >= General_Attack:
            hp = hp - General_Attack
        elif hp >= Soldier_Attack:
            hp = hp - Soldier_Attack
        else:
            hp = hp - Work_Attack
        answer = answer + 1
    return answer