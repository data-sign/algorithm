from collections import deque
import sys

N, M = input().split()
num_lst = [int(i) for i in input().split()]
d = deque(list(range(1, int(N)+1)))
sum_cnt = 0
for i in range(int(M)): 

  # 전체 deque 길이+1 에서 num 위치 정보 나누기 
  # 오른쪽으로 이동 : len(d)-d.index(x)
  if d.index(num_lst[i])/len(d) > 0.5: 
    cnt = len(d)-d.index(num_lst[i])
    for j in range(cnt): 
      d.rotate(1)
    
  # 왼쪽으로 이동 : 인덱스만큼
  else:
    cnt = d.index(num_lst[i])
    for j in range(cnt): 
      d.rotate(-1)

  # 첫 번째 원소 뽑기 
  d.popleft() 
  sum_cnt += cnt
print(sum_cnt)
