import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
dp = a[:]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))