import sys
input = sys.stdin.readline
INF = int(1e9)

# Step 1: 입력 받기
N, M = map(int, input().split())
edges = []
dist = [INF] * (N + 1)
dist[1] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# Step 2: 벨만 포드 알고리즘 수행
for i in range(N):
    for j in range(M):
        cur_node, next_node, cost = edges[j]
        if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
            dist[next_node] = dist[cur_node] + cost

            # N 번째 루프에도 값이 갱신된다면 음수 순환이 존재
            if i == N - 1:
                print(-1)
                sys.exit(0)

# Step 3: 결과 출력
for i in range(2, N + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])

# 벨만 포드 알고리즘의 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느리다.
# 하지만 벨만 포드 알고리즘은 음수 간선이 포함된 경우나,
# 음수 간선에 의한 무한 순환을 감지할 수 있다.