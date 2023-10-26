n, s = map(int, input().split())
x = list(map(int, input().split()))

p1, p2 = 0, 0
su = 0
ans = 100000


while True:
    if su >= s:
        ans = min(ans, p2-p1)
        su -= x[p1]
        p1 += 1
    elif p2 >= n:
        break
    else:
        su += x[p2]
        p2 += 1

if ans == 100000:
    print(0)
else:
    print(ans)
