## DFS

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(x) for x in graph]

# 조사할 리스트
ans = [0]*(N+1)
ans[V] = V  # 처음 시작노드 방문 처리 
node_lst = [V]

def dfs(now): 
    # 이번에 조사할 노드 
    for nxt in graph[now]: 
        # 다음 노드가 방문하지 않았으면 
        if ans[nxt] == 0: 
            # 연결 노드 저장
            ans[nxt] = now
            node_lst.append(nxt)
            # print(node_lst)
            # 탐색 시작  
            dfs(nxt)
           
dfs(V)
print(*node_lst, sep=' ')

from collections import deque
# 조사할 리스트
ans = [0]*(N+1)
ans[V] = V  # 처음 시작노드 방문 처리 
node_lst = [V]

# 조사 순서 큐 
queue = deque()
queue.append(V)
def bfs(): 
    while queue: 
        # 현재 조사할 노드 추출
        now = queue.popleft()
        for nxt in graph[now]: 
            if ans[nxt] == 0: 
                ans[nxt] = now
                queue.append(nxt)
                node_lst.append(nxt)

bfs()
print(*node_lst, sep=' ')