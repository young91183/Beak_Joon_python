
# 입력
n = int(input())
a = set(map(int, input().split()))
m = int(input())
an = list(map(int, input().split()))

for i in an:
    if i in a:
        print(1)
    else:
        print(0)