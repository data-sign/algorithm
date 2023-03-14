sosu_lst = []

N = int(input())
lst = list(map(int, input().split()))

for sosu in lst : 
    soinsu_lst = []
    for i in range(2,sosu+1) : # 2부터 자기자신까지 나눌 때 
        if sosu%i == 0 :      # 나머지가 0인 수가 
            soinsu_lst.append(i)   # 자기 자신 1개 
    if len(soinsu_lst) == 1 : 
        sosu_lst.append(sosu)
print(len(sosu_lst))