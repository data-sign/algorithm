## 백준 : 트럭 
from collections import deque
n, w, l = map(int, input().split()) # n : 트럭 개수, w: 다리 길이, l: 최대 하중  
trunk = list(map(int, input().split()))
# bridge = [0]*w
bridge = deque([0]*w)
i = 0
time = 0
while True: 
    
    left = bridge.popleft()
    if i<=len(trunk)-1:
        if (sum(bridge) + trunk[i] <= l): # 다리 위에 올라간 트럭 무게가 최대 하중보다 작거나 같으면 
            bridge.append(trunk[i])  # 새로운 트럭 추가
            i += 1 
            time += 1
        else: # 기존 트럭 이동 
            bridge.append(0)
            time += 1
    else: 
        bridge.append(0)
        time += 1

    # print(sum(bridge), bridge, i, time)
    if sum(bridge)==0: 
        print(time)
        break 
    # 트럭 추가 
    # 트럭 이동 