import sys
input=sys.stdin.readline
sys.setrecursionlimit(1_000_000)
n = int(input())
graph = []
for i in range(n): 
    graph.append(list(map(int, input().split())))
# print(*graph, sep='\n')

# 메모이제이션을 위한 배열 : (x, y, direction)
memo = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

def move_pipe(x, y, direction, grid, N):

    # print(direction, grid, x, y)
    # 기저 조건: 파이프가 목표 위치에 도달했을 때
    if x == N - 1 and y == N - 1:
        # print("count 증가")
        return 1  # 경우의 수 1 증가

    # 이미 계산된 경우의 수가 있다면 반환
    if memo[x][y][direction] != -1:
        return memo[x][y][direction]
    
    count = 0  # 경우의 수 초기화

    # 현재 방향에 따라 다음 위치로 이동
    if direction == 0:  # 수평
        # 수평으로 이동
        if y + 1 < N and grid[x][y + 1] == 0:  # 오른쪽으로 이동 가능
            count += move_pipe(x, y + 1, 0, grid, N)  # 수평 유지
        # 대각선으로 이동
        if x + 1 < N and y + 1 < N and grid[x + 1][y + 1] == 0 and grid[x][y + 1] == 0 and grid[x + 1][y] == 0:
            count += move_pipe(x + 1, y + 1, 2, grid, N)  # 대각선으로 이동

    elif direction == 1:  # 수직
        # 수직으로 이동
        if x + 1 < N and grid[x + 1][y] == 0:  # 아래로 이동 가능
            count += move_pipe(x + 1, y, 1, grid, N)  # 수직 유지
        # 대각선으로 이동
        if x + 1 < N and y + 1 < N and grid[x + 1][y + 1] == 0 and grid[x][y + 1] == 0 and grid[x + 1][y] == 0:
            count += move_pipe(x + 1, y + 1, 2, grid, N)  # 대각선으로 이동

    elif direction == 2:  # 대각선
        # 수평으로 이동
        if y + 1 < N and grid[x][y + 1] == 0:  # 오른쪽으로 이동 가능
            count += move_pipe(x, y + 1, 0, grid, N)  # 수평으로 이동
        # 수직으로 이동
        if x + 1 < N and grid[x + 1][y] == 0:  # 아래로 이동 가능
            count += move_pipe(x + 1, y, 1, grid, N)  # 수직으로 이동
        # 대각선으로 이동
        if x + 1 < N and y + 1 < N and grid[x + 1][y + 1] == 0 and grid[x][y + 1] == 0 and grid[x + 1][y] == 0:
            count += move_pipe(x + 1, y + 1, 2, grid, N)  # 대각선으로 이동

    # 계산한 경우의 수를 메모이제이션 배열에 저장
    memo[x][y][direction] = count
    return count  # 경우의 수 반환

print(move_pipe(0, 1, 0, graph, n))