from sys import stdin
N = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

s = x.copy()
s = list(set(s))
s.sort()

dic = {s[i] : i for i in range(len(s))}

for i in x:
    print(dic[i], end=" ")

