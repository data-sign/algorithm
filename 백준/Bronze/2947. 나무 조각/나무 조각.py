lst = list(map(int, input().split()))
def compare_lst(lst): 
    for i in range(len(lst)-1): 
        if lst[i] > lst[i+1]: 
            lst[i+1], lst[i] = lst[i], lst[i+1]
            print(*lst)
        else: 
            continue
    return lst

while True:
    if compare_lst(lst) == [1,2,3,4,5]: 
        break
    else: 
        compare_lst(lst)