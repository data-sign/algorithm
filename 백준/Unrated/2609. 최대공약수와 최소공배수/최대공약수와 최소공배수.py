N, M = list(map(int, input().split(' ')))

# 약수를 구하는 함수 생성 
def yaksu(num):
    yaksu_lst = [] 
    for x in range(1, num+1): 
        if num%x==0: 
            yaksu_lst.append(x)
    return yaksu_lst

max_yaksu = max(set(yaksu(N))&set(yaksu(M)))
min_baesu = max_yaksu*(N//max_yaksu)*(M//max_yaksu)
print(max_yaksu, min_baesu, sep='\n')