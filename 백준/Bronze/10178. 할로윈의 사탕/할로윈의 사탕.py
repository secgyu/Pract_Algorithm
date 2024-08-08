t = int(input())

for _ in range(t):
    c, v = map(int, input().split())
    pieces_per_sibling = c // v
    
    pieces_for_dad = c % v
    
    print(f"You get {pieces_per_sibling} piece(s) and your dad gets {pieces_for_dad} piece(s).")
