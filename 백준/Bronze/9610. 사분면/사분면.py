n = int(input())  

count1 = 0  
count2 = 0  
count3 = 0  
count4 = 0  
axis = 0    

for _ in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        count1 += 1
    elif x < 0 and y > 0:
        count2 += 1
    elif x < 0 and y < 0:
        count3 += 1
    elif x > 0 and y < 0:
        count4 += 1

print(f'Q1: {count1}')
print(f'Q2: {count2}')
print(f'Q3: {count3}')
print(f'Q4: {count4}')
print(f'AXIS: {axis}')
