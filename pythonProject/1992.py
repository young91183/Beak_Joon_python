n = int(input())
bread = [] # 표
for i in range(n):
    s = list(map(int, input().strip())) # 하나씩 나누어서 입력 받게 strip 함수 사용
    bread.append(s)

def div(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if bread[x][y] != bread[i][j]: # 만약 시작 지점의 값과 다를 경우
                print("(", end="") # 새로운 괄호를 생성 후 4분할 하여 재귀탐색
                div(x, y, n // 2)
                div(x, y + n // 2, n // 2)
                div(x + n // 2, y, n // 2)
                div(x + n // 2, y + n // 2, n // 2)
                # 이번 문제의 경우 확인하는 사분면의 순서가 정해져 있어 순서를 잘 정하는 것이 중요!
                print(")", end="")
                return


    if bread[x][y] == 1:
        print(1, end="")
    else:
        print(0, end="")

div(0, 0, n)