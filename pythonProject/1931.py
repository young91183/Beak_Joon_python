n = int(input())

time = [i for i in range(24)]
x = []

for i in range(n):
    x.append(list(map(int, input().split())))

x.sort(key=lambda x: (x[1], x[0]))

an = 0

ep = 0

for i in range(n):
    sp = x[i][0]
    if sp >= ep:
        ep = x[i][1]
        an += 1

print(an)

