from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    co = defaultdict(int)
    for _ in range(n):
        name, type = input().split()
        co[type] += 1

    answer = 1
    for count in co.values():
        answer *= (count + 1)  # 해당 종류의 옷을 입거나 안입는 경우 고려

    print(answer - 1)  # 모두 안입는 경우(알몸) 제외
    # print(co)