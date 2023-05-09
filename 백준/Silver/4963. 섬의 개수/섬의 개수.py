#T = int(input()) #테스트케이스의 개수

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def BFS(x,y):           
    queue = [(x,y)]
    matrix[x][y] = 0 # 방문처리

    while queue:
        x,y = queue.pop(0)
#        print("x,y", x,y)
        # 좌, 우, 위, 아래, 대각선 이동 
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 전체 사각형을 넘어가면 멈추기 
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            # 매트릭스가 1(land)면 이동해서 다시 탐색, 방문한 좌표는 0으로 처리
            if matrix[nx][ny] == 1 :
 #               print(nx, ny)
                queue.append((nx,ny))
                matrix[nx][ny] = 0


while True:
    w, h = map(int,input().split())
 
    if (w, h) == (0, 0): 
        break

    else: 
        cnt = 0
        matrix = []

        for i in range(h): 
            matrix.append(list(map(int,input().split())))
  #      print(matrix)

        # x의 이동 -> 행(위아래), y의 이동 -> 열(좌우)
        for a in range(h):
            for b in range(w):
                # land(1)면 좌표이동해서 탐색 
                if matrix[a][b] == 1:
    #                print("a,b", a, b)
                    BFS(a,b)
                    cnt += 1

        print(cnt)