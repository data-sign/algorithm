import sys

input = sys.stdin.readline
n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

# 하얀색, 파란색 
answer = [0,0]

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

                # 재귀대신 경우의 수 나열 
                next_n = n//2
                dfs(x, y, next_n) 
                dfs(x+next_n, y, next_n) 
                dfs(x, y+next_n, next_n) 
                dfs(x+next_n, y+next_n, next_n) 

                return

    # 카운트
    # 하얀색 : 0
    if visited == 0:
        answer[0] += 1
    else:
        answer[1] += 1

dfs(0, 0, n)
print(*answer, sep='\n')