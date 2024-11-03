H, W = map(int, input().split())
h_lst = list(map(int, input().split()))
max_idx = h_lst.index(max(h_lst))

max_left_h = [0]*len(h_lst)
max_right_h = [0]*len(h_lst)

# max_height 구하기 : 왼쪽부터 탐색 (왼쪽부터 하나씩 비교하며 max update)
for i in range(max_idx): 
    if i == 0: 
        max_left_h[i] = h_lst[i]
    else: 
        max_left_h[i] = max(max_left_h[i-1], h_lst[i])

# max_height 구하기 : 오른쪽부터 탐색 (오른쪽부터 하나씩 비교하며 max update)
for i in range(len(h_lst)-1, max_idx, -1): 
    if i == len(h_lst)-1: 
        max_right_h[i] = h_lst[i]
    else: 
        max_right_h[i] = max(max_right_h[i+1], h_lst[i])

# 빗물 구하기 
water = 0
for i in range(max_idx): 
    water += max_left_h[i] - h_lst[i]
for j in range(len(h_lst)-1, max_idx, -1): 
    water += max_right_h[j] - h_lst[j]

print(water)