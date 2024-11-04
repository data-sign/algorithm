def solution(word):
    lst = ['A', 'E', 'I', 'O', 'U']
    from itertools import product
    dictionary = []
    for i in range(1, 6): 
        pm = product(lst, repeat=i)
        for j in pm: 
            print(j)
            dictionary.append(''.join(j))

    dictionary = sorted(set(dictionary))
    answer = dictionary.index(word) + 1
    return answer