N, c, r = map(int, input().split())

sum_ = 0
x, y = 0, 0
while N > 1: 
    n = (2**N)//2

    # 큰 조각으로 나눠 4분면 중 어느 사분면 속하는지에 따라 순서 더 해줌 
    if (c < x + n)&(r < y + n):  # 1사분면
        sum_ += 4**(N-1)*0
        pass
    elif (c < x + n)&(r >=  y + n):  # 2사분면
        sum_ += 4**(N-1)*1
        x, y = x, y+n
    elif (c >= x + n)&(r < y + n):  # 3사분면
        sum_ += 4**(N-1)*2
        x, y = x+n, y
    elif (c >= x + n)&(r >= y + n):  # 4사분면 
        sum_ += 4**(N-1)*3
        x, y = x+n, y+n
    N = N - 1
    # print("sum : ", sum_)

# 가장 작은 2*2 행렬에서 나머지로 최종 순서 더해줌 
if (c%2, r%2)==(0,0):
    answer = sum_
elif (c%2, r%2)==(1,0):
    answer = sum_ + 2
elif (c%2, r%2)==(0,1):
    answer = sum_ + 1
elif (c%2, r%2)==(1,1):
    answer = sum_ + 3
print(answer)