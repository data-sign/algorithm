a =  input().strip().upper()
a_set = list(set(a))

cnt_lst = [a.count(a_set[i]) for i in range(len(a_set))]
max_word = [a_set[i] for i, cnt in enumerate(cnt_lst) if cnt == max(cnt_lst) ]

if len(max_word) > 1 :
    print('?')
else : 
    print(max_word[0])