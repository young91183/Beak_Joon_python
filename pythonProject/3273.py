import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

answer = 0
st = 0
ed = n-1
while st < ed:
    if a[st] + a[ed] == x:
        ed -= 1
        answer += 1
    else:
        if a[st] + a[ed] < x:
            st += 1
        else:
            ed -= 1

print(answer)