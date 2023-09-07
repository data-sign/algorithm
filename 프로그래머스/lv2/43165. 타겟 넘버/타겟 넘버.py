def solution(numbers, target):
    from itertools import product
    n = len(numbers)
    cnt = 0
    for p in list(product([1, -1], repeat=n)): 
        lst = [numbers[i]*p[i] for i in range(n)]
        if sum(lst)==target: 
            cnt += 1
        # print(lst, sum(lst), cnt)
    return cnt