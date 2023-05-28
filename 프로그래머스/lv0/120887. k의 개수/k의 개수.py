def solution(i, j, k):
    cnt = 0
    for s in range(i, j+1):
        cnt += list(str(s)).count(str(k))
    return cnt