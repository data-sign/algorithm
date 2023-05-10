from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

queue = deque()
queue.append(1)
# 조사할 리스트
ans = [0]*(N+1)

def bfs(): 
    while queue: 
        now = queue.popleft()
        # 이번에 조사할 노드 
        for nxt in graph[now]: 
            # 다음 노드가 방문하지 않았으면 
            if ans[nxt] == 0: 
                # 연결 노드 저장
                ans[nxt] = now
                # print(ans)
                # 탐색 시작  
                queue.append(nxt)
           
bfs()

print(len(ans[2:]) - ans[2:].count(0))