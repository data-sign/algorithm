import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [-1 for i in range(n)]

# 입력 받은 배열 arr 탐색 
for i in range(len(arr)):
    # stack의 맨 위 값이 해당 숫자 (arr[i]) 보다 작으면 반복하여 stack에 쌓인 인덱스에 해당하는 답 리스트에 오큰수(arr[i]) 반영    
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)