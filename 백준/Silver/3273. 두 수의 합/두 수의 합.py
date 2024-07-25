import sys
input = sys.stdin.readline


def count_sum(numbers, target_sum):
    numbers.sort()
    left, right = 0, len(numbers) - 1
    count = 0

    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target_sum:
            count += 1
            left += 1
            right -= 1
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1
    return count


n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

print(count_sum(numbers, x))
