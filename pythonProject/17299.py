import sys
from collections import Counter

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
c = Counter(s)  # 각 숫자의 등장 횟수를 계산하여 딕셔너리에 저장

stack = []  # 스택을 사용할 리스트
ngf = [-1] * n  # 결과를 저장할 리스트, 모든 원소의 오등큰 수를 -1로 초기화

# 수열을 오른쪽 부터 순회하여 오등큰수 계산
for i in range(n):
    while stack and c[s[stack[-1]]] < c[s[i]]:
        ngf[stack.pop()] = s[i] # 현재 원소의 오등큰 수 설정
    stack.append(i)  # 현재 원소의 인덱스를 스택에 추가

# 결과 출력
print(' '.join(map(str, ngf)))
