def solution(emergency):
    lst = [0]*len(emergency)
    for i in range(len(emergency)): 
        lst[i] = sorted(emergency, reverse=True).index(emergency[i])+1
    return lst