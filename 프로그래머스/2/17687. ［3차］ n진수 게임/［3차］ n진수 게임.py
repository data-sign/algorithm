def solution(n, t, m, p):

    alpha_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    ## n 진법 함수
    def get_n_num(num, n): 
        # 몫 : quotient, 나머지 : remainder
        n_num = ''
        while True: 
            if num == 0: 
                break 

            r = num%n
            if r >= 10: 
                r = alpha_dict[r]
            n_num += str(r)
            num = num//n

        return n_num[::-1]

    ## 말해야 하는 숫자 n 진법으로 변환하여 하나의 문자열로 나타내기 
    total_num = '0'  
    for num in range(1, m*t): 
        total_num += get_n_num(num, n)   # 011011100101110111

    ## 튜브가 말하는 순서에 따라 최종 result 구하기 
    total_num = total_num[p-1:]
    result = ''
    cnt = 0
    for i in range(0, len(total_num), m):
        if cnt == t: 
            break
        result += total_num[i]
        cnt += 1
    return result