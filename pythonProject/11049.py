import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]


for l in range(1, n): # l은 현재 고려하고 있는 행렬들의 범위 (즉, 연속된 l개의 행렬에 대해 고민)
    for i in range(n-l): # i는 시작하는 행렬의 인덱스

        j = i + l # 중간 지점인 k를 선택, 최소 연산을 찾음

        min_count = float('inf') # 최소 연산을 저장할 변수 초기화

        for k in range(i, j):

            # dp[i][k]: i부터 k까지의 부분 문제에서 필요한 최소 연산 수
            # dp[k+1][j]: k+1부터 j까지의 부분 문제에서 필요한 최소 연산 수
            # matrix[i][0]*matrix[k][1]*matrix[j][1]: i~k까지와 k+1~j까지 곱했을 때 추가되는 연산 수
            count = dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]

            min_count = min(min_count, count)  # 현재까지 계산된 최소 연산과 비교하여 갱신

        dp[i][j] = min_count  # 현재 범위(i~j)에서 필요한 최소 연산 수 저장

print(dp[0][n-1])
