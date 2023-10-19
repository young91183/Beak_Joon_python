import heapq
import sys


def dijkstra(start):
    # 시작노드에 대해서 초기화
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [1e9] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

for i in range(1, V + 1):
    print("INF" if distance[i] == 1e9 else distance[i])
