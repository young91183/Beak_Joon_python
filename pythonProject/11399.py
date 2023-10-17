n = int(input())
p = list(map(int, input().split()))

p.sort()
l = len(p)
an = 0
for i in range(l):
    for j in range(i+1):
        an += p[j]

print(an)