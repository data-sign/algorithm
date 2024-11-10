n = int(input())
count = 0
# 5로 크게 나누고 안 나눠지면 5의 개수를 줄임. 
five = n//5
two = 0
while True: 
    remain = (n - (5*five) - (2*two))
    if five < 0: 
        print(-1)
        break
    if remain == 0 :
        print(five+two) 
        break 
    if remain%2 == 1: 
        five -= 1
    else: 
        two = remain//2