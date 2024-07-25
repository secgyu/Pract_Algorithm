room = input()

digit_count = {str(i): 0 for i in range(10)}

for digit in room:
    digit_count[digit] += 1

six_nine_count = digit_count['6'] + digit_count['9']
digit_count['6'] = (six_nine_count + 1) // 2
del digit_count['9']

max_sets = max(digit_count.values())
print(max_sets)
