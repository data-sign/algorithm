from collections import deque

def bfs(n, k):
    q = deque([(n, 0)])  # (위치, 시간)
    visited = [-1] * 100001  # 방문 여부와 시간을 동시에 체크
    visited[n] = 0

    while q:
        pos, time = q.popleft()

        if pos == k:
            return time

        # 순간이동
        if 0 <= pos * 2 <= 100000 and (visited[pos * 2] == -1 or visited[pos * 2] > time):
            q.appendleft((pos * 2, time))  # 시간 증가 없이 맨 앞에 추가
            visited[pos * 2] = time

        # 걷기 (앞으로, 뒤로)
        for next_pos in (pos - 1, pos + 1):
            if 0 <= next_pos <= 100000 and (visited[next_pos] == -1 or visited[next_pos] > time + 1):
                q.append((next_pos, time + 1))
                visited[next_pos] = time + 1

n, k = map(int, input().split())
print(bfs(n, k))