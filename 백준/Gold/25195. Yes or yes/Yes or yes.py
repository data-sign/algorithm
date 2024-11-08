import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(now_v):
    # 현재 정점이 팬클럽 곰곰이가 있는 정점이거나 이미 방문한 정점이라면 종료
    if visited[now_v] or now_v in is_bear:
        return False

    visited[now_v] = True

    # 현재 정점이 더 이상 갈 수 없는 정점이라면 "yes" 출력
    if not graph[now_v]:
        print("yes")
        exit(0)

    # 다음 정점으로 이동하여 DFS 수행
    for next_v in graph[now_v]:
        if next_v not in is_bear and not visited[next_v]:
            if dfs(next_v):  # 다음 정점에서 "yes"가 출력되면 종료
                return True

    visited[now_v] = False  # 백트래킹
    return False

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    
    # 그래프 구성
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S = int(input())
    is_bear = set(map(int, input().split()))  # 팬클럽 곰곰이가 있는 정점 집합

    # DFS 시작
    dfs(1)
    print("Yes")  # 모든 경로에서 팬클럽 곰곰이를 만날 수 있는 경우