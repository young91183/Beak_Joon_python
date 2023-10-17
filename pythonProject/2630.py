n = int(input())
an = [0, 0]
def pd(x_l, y_l, num):
    global  x, an
    sp = x[x_l][y_l]
    if num == 1:
        an[sp] += 1
        return

    for i in range(num):
        for j in range(num):
            if x[x_l+i][y_l+j] != sp:
                pd(x_l, y_l, num // 2)  # 2사분면
                pd(x_l, y_l + num // 2, num // 2) # 1사분면
                pd(x_l + num // 2, y_l, num // 2) # 3사분면
                pd(x_l + num // 2, y_l + num // 2, num // 2) # 4사분면
                return # 분할을 했다는 건 답이 없다는 뜻 리턴
    an[sp] += 1
    return

x = []
for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)

pd(0, 0, n)

print(an[0], an[1], sep="\n")
