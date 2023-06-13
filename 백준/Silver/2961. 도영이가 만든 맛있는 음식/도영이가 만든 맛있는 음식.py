from itertools import combinations

def sum_and_mul(arr): 
    sum_, mul_ = 0, 1
    for row in arr: 
        mul_ *= row[0]
        sum_ += row[1]
    #print(sum_, mul_)
    return abs(sum_ - mul_)


N = int(input())  # 재료 개수
arr = []
for _ in range(N): 
    ingredient = list(map(int, input().split()))
    arr.append(ingredient)

result_lst = []

# 재료 N개의 조합 
for i in range(1, N+1): 
    # N개씩 뽑은 combination 
    combi = list(combinations(arr, i))
    for x in combi: 
        result = sum_and_mul(x)
        result_lst.append(result)
print(min(result_lst))