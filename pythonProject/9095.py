# 테스트 케이스 개수 T 입력 받기
T = int(input())

# 테스트 케이스만큼 반복
for _ in range(T):
    # 정수 n 입력 받기
    n = int(input())

    # DP 테이블 초기화 (0으로 이루어진 길이 (n+1)의 리스트 생성)
    dp = [0] * (n + 1)

    # 초기 조건 설정 (1, 2, 3은 각각 자신을 만드는 방법이 하나씩 있음)
    for i in range(1, min(n + 1, 4)):
        if i == 1 or i == 2:
            dp[i] = i
        else:
            dp[i] = 4

    # 점화식에 따라 DP 테이블 갱신
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


    print(dp[n])  # 결과 출력
