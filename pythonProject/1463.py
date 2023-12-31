# 입력값 받기
n = int(input())

dp = [0] * (n + 1)

# 2부터 n까지 각 숫자에 대해 최소 연산 횟수 계산
for i in range(2, n + 1):

    dp[i] = dp[i-1] + 1

    if i % 2 == 0:  # 만약 숫자가 2로 나누어 떨어진다면, 현재 저장된 최소 연산 횟수와 비교하여 더 작은 값을 저장
        dp[i] = min(dp[i], dp[i//2] + 1)

    if i % 3 == 0:  # 만약 숫자가 3으로 나누어 떨어진다면, 현재 저장된 최소 연산 횟수와 비교하여 더 작은 값을 저장
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
