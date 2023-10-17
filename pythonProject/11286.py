import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
        # 튜플로 x값의 절댓값과 함께 push 하게 되면 절대값 기준으로 먼저 정렬되고,
        # 그 이후에 x값이 작은 순서대로 정렬됨
