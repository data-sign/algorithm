import sys 
input = sys.stdin.readline
n = int(input())

dp = [0]*100
dp[0] = 0 
dp[1] = 1

for n in range(2, n+1): 
    dp[n] = dp[n-1] + dp[n-2]
    # print(f"dp[{n}]: {dp[n]}")
    
print(dp[n])