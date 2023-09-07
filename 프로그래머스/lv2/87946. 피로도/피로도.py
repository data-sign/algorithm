def solution(k, dungeons):
    from itertools import permutations
    
    ## 던전 가는 방법 순열 (중복 허용)
    max_cnt = 0
    
    n = len(dungeons)
    for p in permutations(dungeons, n):
        cnt = 0
        hp = k
        for dg in p: 
            if hp >= dg[0]: 
                cnt += 1
                hp -= dg[1]
        if max_cnt < cnt: 
            max_cnt = cnt 

    return max_cnt