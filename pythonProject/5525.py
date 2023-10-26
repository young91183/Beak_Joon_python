N = int(input())  # 'IOI' 반복 횟수
M = int(input())  # 전체 문자열 길이
S = input()  # 전체 문자열

answer = 0  # 결과값 (PN이 몇 군데 포함되어 있는지)
p_cnt = 0  # 패턴 카운트 ('IOI'가 연속으로 몇 번 나왔는지)
i = 1  # 인덱스 초기값

while i < M - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        p_cnt += 1
        if p_cnt == N:
            p_cnt -= 1
            answer += 1
        i += 2
    else:
        i += 1
        p_cnt = 0
print(answer)