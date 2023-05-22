T = int(input())
for _ in range(T): 
    n = int(input())
    prices = list(map(int, input().split()))
    incomes = 0  # 이익  
    # max_ = prices[0]  
    max_ = prices[-1] # max값 설정 

    for i in range(n-2, -1, -1): 
        # 현재 가격이 미래 가격(다음값 / max) 보다 싸면 산다 -> 싸게 산 만큼 이익으로 더해줌 
        if prices[i] < max_: 
            incomes += max_ - prices[i]
            # print(incomes)
        # 현재 가격이 max 값이면 판다 -> max_ 값 reset -> 이후 값 들 중 max 변경 
        else : 
            max_ = prices[i]
            continue
         
    print(incomes)