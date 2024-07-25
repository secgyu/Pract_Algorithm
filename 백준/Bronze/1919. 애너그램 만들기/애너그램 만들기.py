word1 = input()
word2 = input()

dict1 = {}
dict2 = {}

for char in word1:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

for char in word2:
    if char in dict2:
        dict2[char] += 1
    else:
        dict2[char] = 1

remove = 0

all_char = set(dict1.keys()).union(set(dict2.keys()))

for char in all_char:
    count1 = dict1.get(char, 0)
    count2 = dict2.get(char, 0)
    remove += abs(count1 - count2)

print(remove)