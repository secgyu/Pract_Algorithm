def solution(arr1, arr2):
    x, y, z = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(z)] for _ in range(x)]  # 3*2행렬

    for i in range(x):
        for k in range(z):
            for j in range(y):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    return answer