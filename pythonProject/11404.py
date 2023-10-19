import sys

# 단계 1: 초기화
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float('inf')  # 무한대를 의미하는 값으로 INF 설정
costs = [[INF]*n for _ in range(n)]  # 각 도시 사이의 비용을 저장할 2차원 리스트를 생성하고 모든 값을 무한대로 초기화
for i in range(n):
    costs[i][i] = 0

# 단계 2: 입력값 처리
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())   # 버스 정보 (출발 도시 a, 도착 도시 b, 필요한 비용 c) 입력 받기
    if costs[a-1][b-1] > c:   # 시작 도시와 도착 도시를 연결하는 노선이 여러 개 있는 경우에는 가장 작은 비용만 저장.
        costs[a-1][b-1] = c

# 단계 3: 플로이드-워셜 알고리즘 적용
for k in range(n):     # 각 중간 정점에 대해,
    for i in range(n):     # 각 시작 정점에서,
        for j in range(n):     # 각 종료 정점까지,
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]

# 단계4: 결과 출력
for row in costs:
    for cost in row:
        if cost == INF:
            print(0, end=' ')   # i에서 j로 갈 수 없는 경우에는 그 자리에 '0' 출력.
        else:
            print(cost, end=' ')   # i에서 j로 가는데 필요한 최소 비용 출력.
    print()
