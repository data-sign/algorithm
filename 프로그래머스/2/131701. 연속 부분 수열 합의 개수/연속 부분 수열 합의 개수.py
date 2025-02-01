def solution(lst):
    sum_lst = [0]*len(lst)
    sum_total_lst=[]
    for j in range(len(lst)): 
        sum_lst_new = []
        for i in range(len(lst)): 
            sum_lst_new.append(sum_lst[i] + lst[(i+j)%len(lst)])
            # print(sum_lst_new)
        sum_lst = sum_lst_new
        sum_total_lst.extend(sum_lst)

    return len(set(sum_total_lst))