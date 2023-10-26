T = int(input())
for _ in range(T):
    M, N, x, y = map(int,input().split())
    x -= 1
    y -= 1
    k = x
    while k < M*N:
        if k%N == y:
            print(k+1)
            break
        k += M
        print(k)
    else:
        print(-1)