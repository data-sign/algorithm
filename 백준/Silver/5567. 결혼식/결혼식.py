# 5567 : 결혼식 : https://www.acmicpc.net/problem/5567

# 친구, 친구의 친구 초대 
# 동기 N 명, 학번 1~N, 상근이 학번 1 

N = int(input())
m = int(input())
graph = [[] for i in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
invited = []

# 1번 연결된 그래프 
for x1 in graph[1]: 
    invited.append(x1)
    invited.extend(graph[x1])

print(len(set(invited) - {1}))