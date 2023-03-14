# n 범위 지정 
def isPrime(num):
    if num==1:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

sosu_lst = []
for i in range(2, 123_456*2):
    if isPrime(i): 
        sosu_lst.append(i)

import sys
while True: 
    n = int(sys.stdin.readline())
    if n ==0: 
        break
    else:
        ans = len([x for x in sosu_lst if n < x <= 2*n])
        print(ans)