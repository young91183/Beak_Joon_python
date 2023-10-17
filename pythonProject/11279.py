import heapq  # 힙 라이브러리
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
            # x가 0일 경우, 배열에서 가장 큰 값을 출력하고 값을 배열에서 제거
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)
        # x가 자연수인 경우, 배열에 해당 값을 추가하는 연산을 수행
