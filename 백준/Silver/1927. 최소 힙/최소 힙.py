## 힙정렬 이용 

import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N): 
    x = int(input())
    if x==0: 
        # 리스트가 비어있으면
        if lst == []: 
            print(0)
        else: 
            # 0이면 최솟값 출력 및 제거
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, x) 
    # print(lst)