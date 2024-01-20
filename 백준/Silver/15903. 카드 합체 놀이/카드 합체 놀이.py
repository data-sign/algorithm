n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

# 가장 작은 수를 더하는것이 좋음 

def sum_card(s_lst): 
    sum_ = s_lst[0] + s_lst[1]
    s_lst[0], s_lst[1] = sum_, sum_
    return s_lst

for _ in range(m): 
    n_lst = sorted(n_lst)
    n_lst = sum_card(n_lst)
print(sum(n_lst))