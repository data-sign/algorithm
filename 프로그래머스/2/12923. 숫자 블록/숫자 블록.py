def solution(begin, end):
    answer = []
    #약수 중 가장 큰 수 찾기
    for i in range(begin,end+1):
        if i>1:
            a=1
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    a=j
                    if i//j<=10000000:
                        a=i//j
                        break
            answer.append(a)
        elif i==1:
            answer.append(0)
    return answer