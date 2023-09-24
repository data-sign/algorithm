N = int(input())
t = []
p = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담 X -> 다음날 값 가져옴 
    if i + t[i] > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])