import sys

n, m = map(int, sys.stdin.readline().split())

name_to_num = {}
num_to_name = {}

# 도감 정보 입력 받기
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(m):
    question = sys.stdin.readline().strip()

    # 숫자인 경우 문자로 변환하여 출력하기 (번호-이름)
    if question.isdigit():
        print(num_to_name[int(question)])

    else:  # 문자인 경우 숫자로 변환하여 출력하기 (이름-번호)
        print(name_to_num[question])
