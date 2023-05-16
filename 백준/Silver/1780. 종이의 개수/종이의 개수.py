import sys

input = sys.stdin.readline
n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

answer = [0,0,0]

def dfs(x, y, n):
    """x, y : 좌표값, n : 종이의 차원"""
    global answer 

    # 종이의 시작점 값 = visited 
    visited = paper[x][y]
    # 반복문을 통해 종이를 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 종이의 시작점 값(0,-1,1)과 다른 값과 비교 
            if paper[i][j] != visited:
                # 다르면 3으로 나눈 범위로(3*3) x,y 좌표 재귀적으로 탐색 
                # for k in range(3): 
                #     for l in range(3): 
                #         # k = 0 : (0 + (0*3), 0+(0*3), 3), (0+(0*3), 0+(1*3), 3), (0+(0*3), 0+(2*3), 3) = (0,0,3), (0,3,3), (0,6,3)
                #         # k = 1 : (0 + (1*3), 0+(0*3), 3) .... = (3, 0, 3), (3, 3, 3), (3, 6, 3)
                #         dfs(x + k*(n//3), y + l*n//3, n//3)

                # 재귀대신 경우의 수 나열 
                next_n = n//3
                dfs(x, y, next_n) 
                dfs(x+next_n, y, next_n) 
                dfs(x+(next_n*2), y, next_n) 
                dfs(x, y+next_n, next_n) 
                dfs(x, y+(next_n*2), next_n) 
                dfs(x+next_n, y+next_n, next_n) 
                dfs(x+(next_n*2), y+next_n, next_n) 
                dfs(x+next_n, y+(next_n*2), next_n) 
                dfs(x+(next_n*2), y+(next_n*2), next_n) 

                return

    # 카운트
    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1

dfs(0, 0, n)
print(*answer, sep='\n')