import sys
input = sys.stdin.readline

n = int(input())
step_score = []

for _ in range(n): 
    step_score.append(int(input()))

if n == 1:
    print(step_score[0])  # 계단이 하나면 그대로 출력
    sys.exit()

# n = 6
# step_score = [10, 20, 15, 25, 10, 20]
dp = [0]*300

dp[0] = step_score[0]
dp[1] = step_score[0] + step_score[1]
if n > 2: 
    dp[2] = max(step_score[0]+step_score[2], step_score[1]+step_score[2])  

    for i in range(3, n):
        dp[i] = max(dp[i-3] + step_score[i-1] + step_score[i]
                    , dp[i-2] + step_score[i])
    
print(dp[n-1])