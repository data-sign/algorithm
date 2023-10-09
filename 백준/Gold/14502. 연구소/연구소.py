import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
import copy
# move up right left down
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# spread virus
def spread_virus(matrix, virus_queue, min_cnt):
    # virus count
    cnt = 0
    # visited map
    visited = [[0]*M for _ in range(N)]

    # 중복 count 방지를 위해 초기 바이러스 칸을 visited 처리 
    for x, y in virus_queue: 
        visited[x][y] = 1

    while virus_queue:
        x, y = virus_queue.pop()
        cnt += 1
        for dx, dy in move:
            nx, ny = x+dx, y+dy

            # matrix 벽 안쪽 and not visited
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]!=1 and visited[nx][ny]==0:
                visited[nx][ny] = 1
                virus_queue.append((nx, ny))

            # virus 확산이 기존 확산 개수보다 많으면 break
            if cnt > min_cnt:
                break
    return cnt

# 바이러스 초기 확산 지점, 벽 놓는 조합을 위한 0인 지점 리스트 추출 
wall_lst = []
virus_q = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 2:
            virus_q.append((x, y))
        if graph[x][y] == 0:
            wall_lst.append((x, y))

# 벽 세개 놓는 조합
from itertools import combinations
wall_combi = list(combinations(wall_lst, 3))
# 최대 안전 영역 = 바이러스 최소 
min_cnt = N*M

while wall_combi:
    wall_add = wall_combi.pop()
    matrix = copy.deepcopy(graph)
    virus_queue = copy.deepcopy(virus_q)

    # 벽 설치 
    for x, y in wall_add:
        matrix[x][y] = 1

    virus_cnt = spread_virus(matrix, virus_queue, min_cnt)

    if virus_cnt < min_cnt:
        # print(virus_cnt, matrix, min_cnt, wall_add)
        min_cnt = virus_cnt

# 0인 개수 - 3(벽 세개 설치) - 바이러스 확산 개수(기존 바이러스2 제외)
print(len(wall_lst)-3-(min_cnt-len(virus_q)))