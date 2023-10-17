from collections import deque

# 상자의 가로와 세로 크기 입력 받기
M, N = map(int, input().split())

# 상자 정보 입력 받기
box = [list(map(int, input().split())) for _ in range(N)]

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
# BFS 구현
def bfs():
    while queue:
        x,y=queue.popleft()

        for i in range(4): # 상하좌우 확인
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위 밖인 경우 무시
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue

            # 비어있거나 이미 익은 토마토인 경우 무시
            if box[nx][ny]==-1 or box[nx][ny] == 1:
                continue

            # 해당 위치에 있는 토마토를 익게 함 (현재 일수 + 1)
            box[nx][ny] = box[x][y]+1
            queue.append((nx, ny))


for i in range(N):
    for j in range(M):
        if box[i][j] == 1: #익은 토마토가 있는 위치를 모두 큐에 추가
           queue.append((i, j))


bfs()

max_days = max([max(row) for row in box])

if any(0 in row for row in box):
    print(-1)
elif max_days == -1:
    print(0)
else:
    print(max_days-1)

