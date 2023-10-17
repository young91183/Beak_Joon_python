import sys

N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))

# 가능한 모든 구슬의 무게에 대하여 확인 여부 체크 배열 초기화
check = [[False] * 40001 for _ in range(N+1)]
def dfs(idx, weight):
    global check, weights
    # 이미 확인한 경우 바로 리턴
    if check[idx][weight]:
        return
    check[idx][weight] = True

    # 모든 추에 대하여
    if idx < N:
        # 해당 추를 사용하지 않는 경우
        dfs(idx + 1, weight)
        # 해당 추를 왼쪽에 놓는 경우 (추의 총합이 증가)
        dfs(idx + 1, weight + weights[idx])
        # 해당 추를 오른쪽에 놓는 경우 (추의 총합이 감소)
        dfs(idx + 1, abs(weight - weights[idx]))

dfs(0, 0)

for ball in balls:
    if ball > sum(weights):
        print('N', end=' ')
    elif check[N][ball]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
