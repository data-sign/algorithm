import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 설정
input = sys.stdin.readline  # 입력을 빠르게 받기 위한 설정

# 정점의 수, 간선의 수, 시작 정점 입력
n, m, r = map(int, input().split())
# 인접 리스트 초기화 (1부터 n까지 사용하기 위해 n+1 크기로 생성)
graph = [[] for _ in range(n + 1)]
# 방문 순서를 저장할 리스트 초기화 (0이면 방문하지 않음)
visited = [0] * (n + 1)

# 방문 순서를 기록할 변수 초기화
visit_order = 1

def dfs(graph, v, visited):
    global visit_order
    visited[v] = visit_order  # 현재 정점을 방문했음을 기록
    visit_order += 1  # 다음 방문 순서 증가

    # 현재 정점 v의 인접 정점들을 순회
    for neighbor in graph[v]:
        if visited[neighbor] == 0:  # 방문하지 않은 정점인 경우
            dfs(graph, neighbor, visited)  # 재귀적으로 DFS 호출

# m개의 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로의 간선 추가
    graph[b].append(a)  # b에서 a로의 간선 추가 (양방향)

# 각 정점의 인접 리스트를 오름차순으로 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 탐색 시작
dfs(graph, r, visited)

# 각 정점의 방문 순서 출력 (1부터 n까지)
for i in range(1, n + 1):
    print(visited[i])