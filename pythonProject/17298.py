import sys

def gogo():
    # 수열의 크기 n 입력 받기
    n = int(sys.stdin.readline())
    # 수열 a의 원소들 입력 받기
    a = list(map(int, sys.stdin.readline().split()))
    s = [] # 스택
    r = [-1 for _ in range(n)]
    s.append(0)
    i = 1

    while s and i < n:
        while s and a[s[-1]] < a[i]: # 현재 원소가 스택 맨 위의 원소보다 크다면
            r[s[-1]] = a[i]  # 해당 위치의 결과값을 현재 원소로 업데이트
            s.pop()  # 오큰수를 찾았으므로 스택에서 제거

        s.append(i)  # 현재 인덱스를 스택에 추가
        i += 1  # 다음 원소로 이동

    for i in range(n):
        print(r[i], end=" ")  # 각 위치의 오큰수 출력

gogo()
