def solution(line):
    answer = []
    stars = set()
    for i in range(len(line)):
        for j in range(i+1, len(line)):

            a, b, e = line[i]
            c, d, f = line[j]

            if (a * d) - (b * c) != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
            
            if int(x) == x and int(y) == y:
                x = int(x)
                y = int(y)
                stars.add((x, y))
    
    min_X = min([star[0] for star in stars])
    max_X = max([star[0] for star in stars])

    min_Y = min([star[1] for star in stars])
    max_Y = max([star[1] for star in stars])

    for y in range(max_Y, min_Y-1, -1):
        one_line = ""
        for x in range(min_X, max_X+1):
            if (x,y) in stars:
                one_line += "*"
            else:
                one_line += "."
        answer.append(one_line)
    
    return answer