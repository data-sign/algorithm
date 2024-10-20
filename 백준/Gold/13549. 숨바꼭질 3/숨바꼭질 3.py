from collections import deque

def bfs(n, k):
    q = deque([n])  # 위치만 저장
    visited = [-1] * 100001  # 방문 여부와 시간을 동시에 체크
    visited[n] = 0

    while q:
        pos = q.popleft()

        if pos == k:
            return visited[pos]

        # 순간이동
        if 0 <= pos * 2 <= 100000 and visited[pos * 2] == -1:
            q.appendleft(pos * 2)  # 순간이동은 큐의 앞에 추가
            visited[pos * 2] = visited[pos]  # 시간 증가 없음

        # 걷기 (앞으로, 뒤로)
        for next_pos in (pos - 1, pos + 1):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                q.append(next_pos)
                visited[next_pos] = visited[pos] + 1

n, k = map(int, input().split())
print(bfs(n, k))