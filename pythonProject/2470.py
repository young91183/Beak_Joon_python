import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
st = 0
ed = n-1

su = abs(arr[st] + arr[ed])
answer = [arr[st], arr[ed]]

while st < ed:
    su_n = arr[st] + arr[ed]
    if abs(su_n) < su:
        su = abs(su_n)
        answer = [arr[st], arr[ed]]
    elif su_n == 0:
        answer = [arr[st], arr[ed]]
        break

    if su_n > 0:
        ed -= 1
    else:
        st += 1

print(answer[0], answer[1])
