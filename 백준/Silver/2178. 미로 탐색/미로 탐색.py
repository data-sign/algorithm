from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):           
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # print("x,y", x,y)

        # 좌, 우, 위, 아래 이동 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 전체 사각형을 넘어가면 멈추기 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 매트릭스가 1이면 이동해서 다시 탐색, 방문한 좌표는 0으로 처리 -> 방문한 칸의 수를 넣음 
            if matrix[nx][ny] == 1 :
                # print(nx, ny)
                queue.append((nx,ny))
                matrix[nx][ny] = matrix[x][y] + 1
    
    return matrix[n-1][m-1]


n, m = map(int,input().split())

matrix = []

for i in range(n): 
    matrix.append(list(map(int, input())))
# print(matrix)

# x의 이동 -> 행(위아래), y의 이동 -> 열(좌우)
print(BFS(0,0))