n, x = map(int, input().split())
lst = list(map(int, input().split()))
# 매번 Sum 할 수 없으니, 빼야 할 숫자만 빼고, 더할 숫자만 더하자 
init_sum = sum(lst[:x])
max_sum = init_sum
cnt = 1
sum_dict = {max_sum:1}
for i in range(n-x): 
    minus_value = lst[i]
    plus_value = lst[i+x]
    init_sum -= minus_value
    init_sum += plus_value
    if max_sum <= init_sum: 
        # 최대 방문자 수와 겹치는 기간 카운트 
        if max_sum == init_sum: 
            cnt += 1
        # 최대 방문자 갱신 시 겹치는 카운트 초기화
        else: 
            cnt = 1
        max_sum = init_sum 
        sum_dict[max_sum] = cnt
        # print(i,plus_value,max_sum, sum_dict)

if max_sum == 0: 
    print('SAD')
else: 
    print(max_sum, sum_dict[max_sum], sep='\n')