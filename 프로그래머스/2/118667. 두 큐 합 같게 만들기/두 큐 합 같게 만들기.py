def solution(queue1, queue2):
    from collections import deque

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    total_sum = sum_q1+sum_q2
    
    if total_sum%2==0: 
        goal = total_sum//2 
    # 합이 홀수면 -1 return 
    else:  
        return -1

    cnt = 0

    def fn_pop_insert(pop_queue, insert_queue):

        x = pop_queue.popleft()
        insert_queue.append(x)
        return pop_queue, insert_queue

    while sum_q1 != sum_q2: 
        if sum_q1 > sum_q2: 
            x = q1.popleft()
            q2.append(x)
            sum_q1 -= x
            sum_q2 += x
        else: 
            x = q2.popleft()
            q1.append(x)
            sum_q2 -= x
            sum_q1 += x

        # q1, q2가 비어 있으면 -1 return 
        if not q1 or not q2: 
            return -1

        cnt += 1
        if cnt > len(queue1)*3: 
            return -1
        # print(q1, sum(q1), '\n', q2, sum(q2), cnt)
    return cnt