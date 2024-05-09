def solution(my_string):
    character = ''
    
    for i in my_string:
        if i.isdigit():
            character += i
    
    sorted_characters = sorted(character)
    
    return [int(num) for num in sorted_characters]

