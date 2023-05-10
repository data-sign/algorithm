dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):           
    queue = [(x,y)]
    matrix[x][y] = 0 # 방문처리
    home_cnt = 0

    while queue:
        x,y = queue.pop(0)
        # print("x,y", x,y)
        home_cnt += 1

        # 좌, 우, 위, 아래, 대각선 이동 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 전체 사각형을 넘어가면 멈추기 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 매트릭스가 1(land)면 이동해서 다시 탐색, 방문한 좌표는 0으로 처리
            if matrix[nx][ny] == 1 :
                # print(nx, ny)
                queue.append((nx,ny))
                matrix[nx][ny] = 0

    return home_cnt


N = int(input())

# 단지 수
cnt = 0 
matrix = []
home_cnt_lst = []

for i in range(N): 
    matrix.append(list(map(int,input())))
# print(matrix)

# x의 이동 -> 행(위아래), y의 이동 -> 열(좌우)
for a in range(N):
    for b in range(N):
        # land(1)면 좌표이동해서 탐색 
        if matrix[a][b] == 1:
            # print("a,b", a, b)
            home_cnt_lst.append(BFS(a,b))
            cnt += 1

print(cnt)
print(*sorted(home_cnt_lst), sep='\n')