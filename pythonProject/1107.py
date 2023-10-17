import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bk = list(map(int, input().split()))

mc = abs(100 - n)  # 초기 횟수 (최다일 경우 가정)

for i in range(1000001):  # 0부터 1000000까지의 숫자를 대상으로 순회
    cnt = str(i)
    for j in range(len(cnt)):  # 숫자 cnt의 각 자리수를 확인
        if int(cnt[j]) in bk:  # 고장난 버튼이라면 중단
            break
    else:
        mc = min(mc, abs(int(cnt) - n) + len(cnt))  # 최소 횟수 갱신

print(mc)
