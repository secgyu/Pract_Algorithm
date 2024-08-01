T = int(input())

for _ in range(T):
    N = int(input())
    max_liquor = -1
    max_school = ""
    
    for _ in range(N):
        school, liquor = input().split()
        liquor = int(liquor)
        
        if liquor > max_liquor:
            max_liquor = liquor
            max_school = school
    
    print(max_school)
