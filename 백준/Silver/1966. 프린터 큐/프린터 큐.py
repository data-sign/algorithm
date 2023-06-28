from collections import deque

T = int(input())
for _ in range(T): 
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    lst = deque(lst)
    index_queue = list(range(N))
    index_queue = deque(index_queue)

    cnt = 0
    answer = []
    # 중요도 계산
    while lst:  
        # 중요도 문서가 max인 것이 앞으로 올때까지 반복 
        if lst[0] == max(lst): 
            lst.popleft()
            # answer.append(index_queue.popleft())
            # print("answer", answer)
            print_idx = index_queue.popleft()
            cnt += 1
            if print_idx == M: 
                print(cnt)
                break
        else: 
            lst.append(lst.popleft())
            index_queue.append(index_queue.popleft())
        # print("lst", lst)