current_people = 0
max_people = 0

for _ in range(4):
    off, on = map(int, input().split())
    
    current_people -= off
    current_people += on
    
    if current_people > max_people:
        max_people = current_people

print(max_people)
