count = int(input())
answer = count
for i in range(count):
    word = input()
    my_set = set()
    for j in range(0, len(word)-1):
        my_set.add(word[j])
        if word[j] != word[j+1]:
            if word[j+1] in my_set:
                answer = answer - 1
                break
print(answer)