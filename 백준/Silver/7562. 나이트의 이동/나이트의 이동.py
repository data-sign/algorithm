from collections import deque
T = int(input())
for _ in range(T):
    I = int(input())
    x, y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    graph = []
    visited = []
    for i in range(I): 
        graph.append([0]*I)
        visited.append([0]*I)
        
    queue = deque()
    queue.append((x, y))

    while queue: 
        x, y = queue.popleft()
        
        if x == end_x and y == end_y: 
            print(graph[x][y])
            break
        move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (2, -1), (1, -2)]
        for dx, dy in move: 
            nx, ny = x+dx, y+dy
            if 0<=nx<I and 0<=ny<I and not visited[nx][ny]: 
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
                # print(queue)
                # print(*graph, sep='\n')