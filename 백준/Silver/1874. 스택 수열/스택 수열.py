from collections import deque

answer_stack = []
N = int(input())
for _ in range(N): 
    answer_stack.append(int(input()))

num_lst = list(range(N, 0, -1))  # [8, 7, 6, 5, 4, 3, 2, 1]
answer_stack = deque(answer_stack) # deque([4,3,6,8,7,5,2,1])
answer = []   # (+), (-)
stack_ = []

# 처음 스택에 다 넣음 
for _ in range(answer_stack[0]):
    stack_.append(num_lst.pop()) # [8, 7, 6, 5]
    answer.append("+")

## 오름차순으로 스택에 넣어야 함 
while answer_stack: 
    answer_num = answer_stack.popleft()
    if stack_: 
        stack_num = stack_.pop()
        # print(stack_num, answer_num)
        if stack_num == answer_num: 
            answer.append("-") 
        # 오름차순보다 더 높은 숫자가 있으면 push 
        elif stack_num < answer_num : 
            stack_.append(stack_num)
            while num_lst: 
                num = num_lst.pop()
                # print("num, answer_num", num, answer_num)
                if num < answer_num: 
                    stack_.append(num)
                    answer.append("+")
                elif num == answer_num: 
                    answer.append("+")
                    answer.append("-")
                else:  
                    num_lst.append(num)
                    break
        else: 

            answer = ["NO"]
            break
    # 스텍이 비어있으면
    else: 
        while num_lst: 
            num = num_lst.pop()
            # print("num, answer_num", num, answer_num)
            if num < answer_num: 
                stack_.append(num)
                answer.append("+")
            elif num == answer_num: 
                answer.append("+")
                answer.append("-")
            else:  
                num_lst.append(num)
                break

    # print(answer_num, stack_, num_lst, answer)
print(*answer, sep='\n')