def solution(k, ranges):
    def ubaksu(k):
        if k%2==0: 
            k/=2 
        else: 
            k=k*3+1
        return k
    k_lst = [k]
    while k > 1:
        k = ubaksu(k)
        k_lst.append(k)

    ## 2. 정적분
    result_dict = {}
    answer = []
    n = len(k_lst)-1
    for a, b in ranges:
        b = n+b
        # print(a, b)
        if a == b: 
            result = 0
        elif a > b: 
            result = -1
        else: 
            result = 0
            for i in range(a, b): 
                # 딕셔너리 없으면 넓이 구해서 넣기
                if i in result_dict: 
                    result += result_dict[i]
                else:
                    result_dict[i] = (k_lst[i]+k_lst[i+1])/2 
                    result += result_dict[i]
        answer.append(result)
    return answer