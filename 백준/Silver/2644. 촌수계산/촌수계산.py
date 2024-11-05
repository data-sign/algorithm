import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 설정

n = int(input())
start, end = map(int, input().split())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]  

# m개의 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로의 간선 추가
    graph[b].append(a)  # b에서 a로의 간선 추가 (양방향)

visited = [0]*(n+1)
count = 0

def dfs(graph, v, visited):
    global count 
    visited[v] = count
    count += 1
    if v == end: 
        return visited[v]

    for i in graph[v]: 
        if visited[i] == 0: 
            # print(visited)
            result = dfs(graph, i, visited)
            if result is not None: 
                return result
    count -= 1
    return None
            
answer = dfs(graph, start, visited)
if answer is not None: 
    print(answer)
else: 
    print(-1)