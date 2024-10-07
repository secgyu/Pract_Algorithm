def solution(p):
    #1
    if p == '': return p
    
    #2
    def balance(w):
        count = 0
        for i in range(len(w)):
            if w[i] == '(': count += 1
            else : count -= 1
            if count == 0:
                return w[:i+1], w[i+1:]
    #3
    def correct(w):
        count = 0
        for char in w:
            if char == '(': count += 1
            else : count -= 1
            if count < 0: return False
        return count == 0
    
    #4
    def rec(s):
        if s == "":
            return ""
        
        u, v = balance(s)
        
        if correct(u):
            return u + rec(v)
        else:
            result = '(' + rec(v) + ')'
            u = u[1:-1]
            u = ''.join(')' if c == '(' else '(' for c in u)
            return result + u
    return rec(p)