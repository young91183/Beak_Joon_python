n, m, k = map(int, input().split())
x = []
for i in range(n):
    x.append(input())
min_count = k*k

for row in range(n - k + 1):
    for col in range(m - k + 1):
        c_1 = 0
        c_2 = 0
        for i in range(k):
            for j in range(k):
                if (i + j) % 2 == 0:
                    if x[row + i][col + j] == 'W':
                        c_1 += 1
                    else:
                        c_2 += 1
                else:
                    if x[row + i][col + j] == 'W':
                        c_2 += 1
                    else:
                        c_1 += 1
        min_count = min(min_count, c_1, c_2)

print(min_count)
