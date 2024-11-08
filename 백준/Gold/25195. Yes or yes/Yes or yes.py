# 25195
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(now_v):
    if visited[now_v] or now_v in is_bear:
        return
    visited[now_v] = True

    if not graph[now_v]:
        print("yes")
        exit(0)

    for next_v in graph[now_v]:
        if next_v not in is_bear and not visited[next_v]:
            dfs(next_v)
            visited[next_v] = False


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

S = int(input())
is_bear = {}
s = list(map(int, input().split()))
for _s in s:
    is_bear[_s] = True

dfs(1)
print("Yes")