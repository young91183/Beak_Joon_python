import heapq  # 우선순위 큐
import sys

def dijkstra(start):  # 다익스트라 알고리즘 함수
    q = []  # 우선순위 큐를 선언합니다.
    heapq.heappush(q, (0, start))  # 시작 노드의 거리(0)와 시작 노드 번호를 튜플로 묶어 우선순위 큐에 추가
    distance[start] = 0  # 시작노드에서 자기 자신으로 가는 비용

    while q:
        dist, now = heapq.heappop(q)  # 현재 가장 짧은 거리의 노드 정보를 꺼내서
        if distance[now] < dist:
            continue   # 만약 현재 꺼낸 노드가 이미 처리된 적이 있는 노드라면 무시

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:   # 해당 노드를 거치는 게 기존의 최단 경로보다 짧으면
                distance[i[0]] = cost   # 최단 경로 테이블을 갱신하고,
                heapq.heappush(q, (cost, i[0]))   # 그 정보를 우선 순위 큐에 추가

V, E = map(int, input().split())   # 정점과 간선의 개수 입력 받기
start = int(input())   # 시작 정점 번호 입력 받기
graph = [[] for _ in range(V + 1)]   # 각 정점마다 연결되어 있는 정점들을 저장하는 리스트 생성

distance = [1e9] * (V + 1)   ## 최단거리 테이블 초기화 - 처음에는 모든 위치까지의 최단거리를 '무한'으로 설정

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w)) ## u에서 v로 가는 가중치 w인 간선 추가

dijkstra(start)

for i in range(1,V+1):
    print("INF" if distance[i]==1e9 else distance[i]) ## 결과 출력