n = int(input())
r = list(map(int, input().split()))
p = list(map(int, input().split()))

m = p[0]
an = 0
for i in range(n - 1):

    if p[i] < m:
        m = p[i]

    an += m * r[i]

print(an)