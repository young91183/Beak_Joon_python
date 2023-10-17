n, m = map(int,input().split())

not_heard = {input() for _ in range(n)}
not_seen = {input() for _ in range(m)}

# 듣보잡 리스트 생성 (듣지도 보지도 못한 사람: not_heard와 not_seen의 교집합)
dbj = sorted(list(not_heard & not_seen))

print(len(dbj))  # 듣보잡 수 출력

for name in dbj:  # 각각 이름 출력
    print(name)
