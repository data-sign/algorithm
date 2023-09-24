def solution(n, info):
    # 점수 계산 함수 식
    def get_score(info, result): 
        a, l = 0, 0
        lst = [info, result]
        # 0점 맞추는 경우는 계산 X 
        for i in range(10): 
            ## 둘다 0점이면 점수 계산 X 
            if lst[0][i] == 0 and lst[1][i] == 0: 
                continue
            else: 
                if  lst[0][i]<lst[1][i]: 
                    l += 10-i
                elif lst[1][i] <= lst[0][i]: 
                    a += 10-i
        return l-a

    max_score, answer = 0, []
    from itertools import combinations_with_replacement
    for combi in combinations_with_replacement(range(11), n):  # 중복 조합으로 0~10점까지 n개 뽑기
        info2 = [0] * 11  # 라이언의 과녁 점수

        for i in combi:  # combi에 해당하는 화살들을 라이언 과녁 점수에 넣기
            info2[10 - i] += 1
        score = get_score(info, info2)
        # print(info2, get_score(info, info2))
        if max_score < score: 
            max_score = score
            answer = info2
    if max_score == 0: 
        answer = [-1]
    return answer