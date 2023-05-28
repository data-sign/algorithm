def solution(array, n):
    min_ = 100
    for i in array: 
        if abs(i-n) < min_: 
            min_ = abs(i-n)
    answer = n - min_ 
    if answer in array: 
        return answer
    else : 
        return n + min_ 