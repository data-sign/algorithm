import sys
import heapq
input = sys.stdin.readline

abs_heap = []
N = int(input())
for _ in range(N): 
    x = int(input())
    if x == 0: 
        if abs_heap == []: 
            print(0)
        else: 
            # 절대값이 같은개 여러개이면 작은 값 출력 -> 자동 
            print(heapq.heappop(abs_heap)[1]) # 튜플의 두번째 자리에 저장된 실제 원소 값 (x) 출력

    else: 
        heapq.heappush(abs_heap, (abs(x), x))  # 첫번째 원소를 기준으로 우선순위 힙 정렬 
                      