n, m = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]

# 3차원 DP 배열 사용: [행][열][이전 방향]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

# 첫 번째 행 초기화
for j in range(m):
    for d in range(3):
        dp[0][j][d] = map_[0][j]

# DP로 최소 연료 계산
for i in range(1, n):
    for j in range(m):
        for d in range(3):
            for prev_d in range(3):
                if d != prev_d:  # 이전 방향과 다른 경우만 고려
                    new_j = j + (d - 1)  # -1, 0, 1 중 하나
                    if 0 <= new_j < m:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][new_j][prev_d] + map_[i][j])

# 마지막 행에서 최소값 찾기
result = min(min(dp[n-1][j]) for j in range(m))
print(result)