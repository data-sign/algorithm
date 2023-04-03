from collections import deque
import sys
N = int(sys.stdin.readline())
# N = int(input())

# 1번 카드가 제일 위에(마지막 인덱스) 위치
lst = list(range(1, N+1))
lst = deque(lst)
# 두개의 카드가 남을 때까지 반복 
while len(lst) > 2:  
    # 가장 위에 있는 카드 바닥에 버리기 
    lst.popleft()
    # 그다음 위에 있는 카드를 제일 아래에 있는 카드로 옮기기 
    lst.append(lst.popleft())

print(lst[-1])