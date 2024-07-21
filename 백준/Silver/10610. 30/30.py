N = input()
arr = list(N)

if '0' not in arr:
    print(-1)

else:
    arr_sum = sum(int(i) for i in arr)
    if arr_sum % 3 != 0:
        print(-1)
    else:
        arr.sort(reverse=True)
        result = ''.join(arr)
        print(result)
