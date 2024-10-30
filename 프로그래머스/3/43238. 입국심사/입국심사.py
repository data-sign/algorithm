def solution(n, times):

    start = 1
    end = n*max(times)
    answer = 0

    while start <= end: 

        mid = (start + end) // 2
        print(mid)
        # 전체 시간을 이용해 각 심사관마다 이용가능한 수 계산하기 
        cnt = 0
        for i in range(len(times)): 
            cnt += mid//times[i]
        if cnt >= n: # 이용가능한 수가 대기자보다 많거나 같음 -> 시간을 줄여야 함  
            print("이용자 많음", cnt, start, end)
            end = mid - 1
            answer = mid
        else:  # 이용가능한 수가 대기자랑 같거나 적음 -> 
            print("이용자 적음", cnt, start, end)
            start = mid + 1
    return answer