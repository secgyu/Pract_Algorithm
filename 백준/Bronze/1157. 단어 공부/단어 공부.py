word = input().upper()
my_set = list(set(word))
cnt = []

for i in my_set:
    count = word.count(i)
    cnt.append(count)

max_count = max(cnt)
if cnt.count(max_count) > 1:
    print('?')
else:
    print(my_set[(cnt.index(max_count))])
