def solution(balls, share):
    num, num2 = 1, 1
    for i in range(balls, share, -1): 
        num *= i
        num2 *= (i-share)
    answer = num/num2
    return answer