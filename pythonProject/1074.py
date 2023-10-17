def Z(n, x, y):

    if n == 1:
        return 0

    n //= 2

    # 목표 위치가 2사분면에 있는 경우
    if x < n and y < n:
        return Z(n, x, y)

    # 목표 위치가 1사분면에 있는 경우
    elif x < n and y >= n:
        return Z(n, x, y - n) + (n * n)

    # 목표 위치가 3사분면에 있는 경우
    elif x >= n and y < n:
        return Z(n, x - n, y) + (2 * (n * n))

        # 목표 위치가 4사분면에 있는 경우
    else:
        return Z(n, x - n, y - n) + (3 * (n * n))

# 조건들의 순서가 중요 2 -> 1 -> 3-> 4 사분면 순으로 진행

N, r, c = map(int, input().split())

print(Z(2 ** N, r, c))