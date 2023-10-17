from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visit[n] = 1   # 방문 표시 1
    while q:
        x = q.popleft()
        for i in board[x]:
            if visit[i] == 0:    # 방문 X 시
                visit[i] = -visit[x]  # 반대 부호로 방문 표시
                q.append(i)          # 방문한 노드를 큐에 추가
            else:
                if visit[i] == visit[x]:  # 이미 방문한 노드와 현재 노드가 같다면
                    return False  # 이분 그래프가 아님을 반환
    return True  # 이상 없으면 이분 그래프임을 반환

N = int(input())  # 테스트 케이스의 개수 입력
for i in range(N):
    V, X = map(int, input().split())  # 정점 개수 V와 간선 개수 X 입력
    board = [[] for _ in range(V+1)] # 인접 리스트
    visit = [0] * (V + 1)  # 방문 배열
    check = 1  # 이분 그래프인지 아닌지 판별하기 위한 변수

    for _ in range(X):
        a, b = map(int, input().split())  # 간선 정보 입력
        board[a].append(b)  # 양방향 간선이므로 a에서 b로 가는 간선 추가
        board[b].append(a)  # b에서 a로 가는 간선 추가

    for i in range(1, V+1):
        if visit[i] == 0:  # 아직 방문하지 않은 노드인 경우
            if not bfs(i):  # BFS 탐색 결과가 이분 그래프가 아니라면
                check = -1
                break

    print('YES' if check == 1 else 'NO')  # 이분 그래프인지 여부에 따라 결과 출력
