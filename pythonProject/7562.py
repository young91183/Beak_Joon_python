from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 0
    while q:
        a, b = q.popleft()
        if a == ex and b == ey: # 만약 현재 위치가 목표 위치라면 해당 칸까지의 거리 s[ex][ey]를 반환
            return s[ex][ey]
        for i in range(8): # 새로운 위치 (x,y)를 계산하고 체스판 내부에 있는지 확인
            x = a + dx[i]
            y = b + dy[i]
            # 만약 체스판 내부에 있고 아직 방문하지 않았다면 큐에 새로운 위치를 넣고 해당 칸까지의 거리를 현재 칸의 거리 + 1로 설정
            if (0 <= x < l) and (0 <= y < l) and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1


T = int(input())
for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    # 초기화
    s = [[0] * l for _ in range(l)]

    print(bfs(sx, sy, ex, ey))
