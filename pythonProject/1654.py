import sys

k, n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)  # 처음과 끝위치

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    m = (start + end) // 2  # 중간
    lines = 0
    for i in lan:
        lines += i // m  # 분할 된 랜선 수

    if lines >= n:  # 랜선의 개수가 분기점
        start = m + 1
    else:
        end = m - 1
print(end)