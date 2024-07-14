while True:
    n = int(input())
    if n == -1:
        break
    array = []

    for i in range(1, n):
        if n % i == 0:
            array.append(i)
    if sum(array) == n:
        print(n, "=", " + ".join(map(str, array)))
    else:
        print(n, "is NOT perfect.")
