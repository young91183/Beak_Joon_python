def check(x, y, n):
    global bread, m_cnt, z_cnt, p_cnt
    num = bread[y][x]  # 첫 번째 원소를 기준으로 모든 원소가 같은지 확인

    for i in range(x, x + n):
        for j in range(y, y + n):
            if bread[j][i] != num:  # 하나라도 다르면 분할
                for k in range(3):
                    for l in range(3):
                        check(x + k * n//3, y + l * n//3, n//3)
                return

    # 모든 원소가 같으면 해당 숫자 카운트 증가
    if num == -1:
        m_cnt += 1
    elif num == 0:
        z_cnt += 1
    else:
        p_cnt += 1


N = int(input())
bread = [list(map(int,input().split())) for _ in range(N)]
m_cnt = 0
z_cnt = 0
p_cnt = 0
check(0, 0, N)
print(m_cnt)
print(z_cnt)
print(p_cnt)