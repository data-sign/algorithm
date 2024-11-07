from collections import deque
import sys 
input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # N : 도시개수, M : 도로개수, K : 거리정보, X : 출발 도시정보 
graph = [[] for _ in range(N + 1)]

# M개의 간선 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로의 간선 추가

queue = deque()
queue.append(X)
visited = [-1] * (N + 1)  # 거리 정보를 -1로 초기화 (방문하지 않은 도시)
visited[X] = 0  # 출발 도시의 거리는 0

city_lst = []
while queue: 
    v = queue.popleft()
    distance = visited[v] 
    
    # 현재 도시에서 K 거리인 도시를 찾기
    if distance == K: 
        city_lst.append(v)
    
    for i in graph[v]: 
        if visited[i] == -1:  # 방문하지 않은 도시인 경우
            queue.append(i)
            visited[i] = distance + 1  # 이전 거리 + 1

# 결과 출력
city_lst.sort()
if len(city_lst) == 0: 
    print(-1)
else: 
    print(*city_lst, sep='\n')