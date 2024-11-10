s = input()
s2 = s.split('-')
# print(s2)
sum_lst = []
for split_s in s2: 
    # print(split_s)
    if '+' in split_s: 
        split_plus = split_s.split('+')
        sum_lst.append(sum([int(i) for i in split_plus]))
    else: 
        sum_lst.append(int(split_s))
# print(sum_lst)

answer = sum_lst[0]
for i in sum_lst[1:]: 
    answer -= i
print(answer)