x = input().split('-')
an = 0

for i in range(len(x)):
    num = sum(map(int, x[i].split('+')))
    if i != 0:
        an -= num
    else :
        an += num

print(an)

# 반례 1+1 때문에 조금 고민함.