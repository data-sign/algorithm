def solution(board):
    from collections import deque

    # 초기 시작 위치 = R의 위치 
    w, h = len(board[0]), len(board)
    visited = [[0]*w for i in range(h)]
    for i in range(h): 
        for j in range(w):
            if board[i][j] == 'R':
                x, y = i, j
                print(x, y)
                break

    queue = deque()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 0
    queue.append((x, y, 0))
    while queue: 
        init_x, init_y, cnt = queue.popleft()
        visited[init_x][init_y] = 1

        if board[init_x][init_y] == 'G': 
            return cnt

        for direction in directions:
            x, y = init_x, init_y
            # print(direction, x, y)        
            while True: 
                dx, dy = direction[0], direction[1] 
                nx, ny = x + dx, y + dy 
                if 0 > nx or nx >= h or 0 > ny or ny >= w or board[nx][ny] == 'D':   # D 도달할 때까지 x, y 옮기기 
                    break
                else: 
                    x, y = nx, ny


            if visited[x][y] == 0: 
                queue.append((x, y, cnt+1))  # D가 있을 때까지 큐에 삽입 

    return -1