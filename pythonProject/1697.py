from collections import deque

n, k = map(int, input().split())


def bfs(nf, kf):
    if nf >= kf:
        return nf - kf

    mx = 100001
    go = [False] * mx

    dq = deque()
    dq.append(nf)
    time = 0

    while dq:
        for _ in range(len(dq)):
            x = dq.popleft()
            if x == kf:
                return time

            for xa in [x - 1, x + 1, x * 2]:
                if 0 <= xa < mx and not go[xa]:
                    go[xa] = True
                    dq.append(xa)

        time += 1

print(bfs(n, k))

