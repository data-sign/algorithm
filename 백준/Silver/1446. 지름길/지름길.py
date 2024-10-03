
# 시작점부터 각 거리까지의 거리를 담은 리스트에 최소거리르 업데이트 
import sys

n, d = map(int, sys.stdin.readline().split())

dp = [i for i in range(d+1)]

shortcuts = []

for _ in range(n):
    start, dest, length = map(int, sys.stdin.readline().split())
    if dest - start > length:  # 지름길이 진짜 지름길일 때 
        shortcuts.append((start, dest, length))
shortcuts.sort()

for start, dest, length in shortcuts:
    for i in range(1, d+1):
        if dest == i:
            dp[i] = min(dp[i], dp[start]+length)  # 기존 거리값 vs. 지름길 
        else:
            dp[i] = min(dp[i], dp[i-1]+1)  # 지름길 이후 거리도 지름길 기준으로 +1 해서 변경 
print(dp[d])