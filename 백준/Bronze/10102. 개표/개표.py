V = int(input())

votes = input()

count_A = votes.count('A')
count_B = votes.count('B')

if count_A > count_B:
    print('A')
elif count_B > count_A:
    print('B')
else:
    print('Tie')