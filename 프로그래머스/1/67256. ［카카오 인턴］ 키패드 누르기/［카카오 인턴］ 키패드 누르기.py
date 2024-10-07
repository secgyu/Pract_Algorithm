def solution(numbers, hand):
    answer = ''
    key_pad = {
        '1' : (0,0), '2' : (0,1), '3' : (0,2),
        '4' : (1,0), '5' : (1,1), '6' : (1,2),
        '7' : (2,0), '8' : (2,1), '9' : (2,2),
        '*' : (3,0), '0' : (3,1), '#' : (3,2)        
    } 
    
    start_left = key_pad['*']
    start_right = key_pad['#']
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            start_left = key_pad[str(n)]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            start_right = key_pad[str(n)]
        else :
            left_hand = abs(start_left[0] - key_pad[str(n)][0]) + abs(start_left[1] - key_pad[str(n)][1])
            right_hand = abs(start_right[0] - key_pad[str(n)][0]) + abs(start_right[1] - key_pad[str(n)][1])
            
            if left_hand < right_hand:
                answer += 'L'
                start_left = key_pad[str(n)]
            elif left_hand > right_hand:
                answer += 'R'
                start_right = key_pad[str(n)]
            else:
                if hand == 'right':
                    answer += 'R'
                    start_right = key_pad[str(n)]
                else :
                    answer += 'L'
                    start_left = key_pad[str(n)]
    return answer