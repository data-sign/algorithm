# 백준 : 고양이는 많을수록 좋다 
count = 0 
n = int(input())  # 목표 고양이 수 
k = 0  # 현재 고양이 수 
if n == 0: 
    print(0)
    exit()
    
# 생성 
k += 1
count += 1
while True: 
    if k >= n :
        print(count) 
        break 
    k += k 
    count += 1 