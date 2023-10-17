n = int(input())
st = []

for i in range(n):
    st.append(int(input()))

# 1 dfs를 이용한 풀이 하지만 시간 초과
# an = []
# def dfs(stack, start, sum):
#     if start == n-1:
#         an.append(sum)
#         return
#     elif start > n-1:
#         return
#     else :
#         if stack == 1 and start < n - 3:
#             dfs(0, start + 2, sum + st[start+2])
#         elif start < n-2:
#             if start < n-3:
#                 dfs(0, start+2, sum + st[start+2])
#             dfs(1, start + 1, sum + st[start + 1])
#
# dfs(0, 0, st[0])
# dfs(0, 1, st[1])
#
# print(max(an))

# 2 점화식을 이용한 풀이
an = [0] * n

if len(st) <=2:
    print(sum(st))
else:
    an[0] = st[0]
    an[1] = st[1]+ st[0]
    for i in range(2, n):
        an[i] = max(an[i-3] + st[i-1] + st[i], an[i-2]+st[i])
        print(an[i], an[i-3])
    print(an[-1])