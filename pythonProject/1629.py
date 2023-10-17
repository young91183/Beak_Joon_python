import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def dc (a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 1 :
        test = dc(a, b // 2, c)
        return (test * test * a) % c
    else :
        test = dc(a, b // 2, c)
        return (test * test) % c

an = dc(a, b, c)
print(an)