
def explode(s, b):
    stack = []  # 스택 생성

    for char in s:  # 입력 문자열을 한 문자씩 순회
        stack.append(char)  # 스택에 문자 추가

        # 스택의 끝 부분이 폭발 문자열과 일치하면
        if ''.join(stack[-len(b):]) == b:
            for _ in range(len(b)):  # 폭발 문자열 길이만큼 스택에서 문자 제거
                stack.pop()

    result = ''.join(stack)  # 스택에 남은 문자들을 합쳐서 결과 문자열 생성

    if result:  # 결과 문자열이 비어있지 않으면
        return result
    else:
        return "FRULA"  # 결과 문자열이 비어있으면 "FRULA" 반환

s = input().strip()  # 입력 문자열 받고 좌우 공백 제거
b = input().strip()  # 폭발 문자열 받고 좌우 공백 제거

result = explode(s, b)  # 문자열 폭발 함수 호출하여 결과 저장
print(result)  # 결과 출력
