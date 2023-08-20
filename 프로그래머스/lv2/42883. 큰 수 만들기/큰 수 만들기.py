
def solution(number, k):
    from collections import deque
    
    num_lst = deque(number)
    removed_nums = sorted(num_lst)[:k]
    
    answer = []
    cnt = 0
    # 남겨야 하는 숫자
    
    for i in range(len(number)): 
        if num_lst[i] in removed_nums:
            num_lst.popleft()
            continue
        else:
            answer.append(num_lst[i])
        if cnt == k:
            answer.append(num_lst[i:])
            break
    
    return answer