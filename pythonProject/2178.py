from collections import deque

# 상하좌우 움직임을 위한 변수
gx = [-1, 1, 0, 0]
gy = [0, 0, -1, 1]


def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        print(f"데크 날리고 나서 : {dq}")
        for i in range(4):  # 상하좌우 체크
            nx = x + gx[i]
            ny = y + gy[i]

            # 미로 범위 밖으로 나갈 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 무시
            if miro[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                dq.append((nx, ny))
                print(f"데크 확인: {dq}")

        # 도착 지점인 (3 ,5)에 도달 했을 때 큐 상태 출력
        if (3, 5) in dq:
            print(f"도착 지점에서 데크: {dq}")

    return miro[n - 1][m - 1]


n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

print(bfs(0, 0))
