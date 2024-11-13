n = int(input())
scores = [int(input()) for _ in range(n)]

total_decrease = 0
for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        decrease = scores[i] - scores[i + 1] + 1
        scores[i] -= decrease
        total_decrease += decrease

print(total_decrease)