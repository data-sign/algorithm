import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    # 패턴을 만드는 별, 재귀 호출을 끝내는 지점
    if LEN == 1:
        return ['*']
    
    Stars = append_star(LEN//3) 
    L = []  
    
		# 별의 패턴대로 한 줄씩 작성하여 append하여 전체 정사각형을 만든다. 
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
# 한줄씩 건너뛰게 표시하려면 리스트의 각 요소(한 줄)를 \n 연결하여 표시 
print('\n'.join(append_star(n)))