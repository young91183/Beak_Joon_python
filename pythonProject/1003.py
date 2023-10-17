T = int(input())
test_cases = [int(input()) for _ in range(T)]

fibonacci = [(1, 0), (0, 1)] + [None]*39

for i in range(2, 41):
    fibonacci[i] = (fibonacci[i-1][0] + fibonacci[i-2][0], fibonacci[i-1][1] + fibonacci[i-2][1])
# 피보나치 수열을 미리 만들어버리자

for N in test_cases:
    print(*fibonacci[N])
# 만들어진 수열에서 정답을 뽑자
