n, m = map(int, input().split())

x = []
for i in range(n):
    x.append(list(map(int, input().split())))

m, k = map(int, input().split())

y = []
for i in range(m):
    y.append(list(map(int, input().split())))

an = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        temp = 0
        for q in range(m):
            temp += x[i][q] * y[q][j]
        an[i][j] = temp


for i in range(len(an)):
    for j in range(len(an[i])):
        print(an[i][j], end=" ")
    print("")
