def nums(n: int) -> list[list[int]]:
    x, y, c = n - 1, 1, 0
    k = n + 1
    result = [[_ for _ in range(1, n + 1)] for _ in range(n)]
    while k <= n ** 2:
        c += 1
        for _ in range(n - c):
            result[y][x] = k
            k, y = k + 1, y + 1

        x, y = x - 1, y - 1
        for _ in range(n - c):
            result[y][x] = k
            k, x = k + 1, x - 1

        x, y, c = x + 1, y - 1, c + 1
        for _ in range(n - c):
            result[y][x] = k
            k, y = k + 1, y - 1

        x, y = x + 1, y + 1
        for _ in range(n - c):
            result[y][x] = k
            k, x = k + 1, x + 1

        x, y = x - 1, y + 1

    return result


res = nums(5)
for row in res:
    for col in row:
        print(f'{col:>3}', end=' ')
    print()

