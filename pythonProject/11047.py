n, k = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    if k>= a[i]:
        e = k // a[i]
        count += e
        k -= a[i] * e
    if k == 0:
        break

print(count)

# k -= a[i] * count 이부분 나머지여서 인터넷에서는 나머지로 풀었...