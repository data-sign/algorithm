import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
from itertools import permutations

min_, max_ =  int(1e9), -int(1e9)
operator = '+'*plus + '-'*minus + '*'*mul + '/'*div
for o in permutations(operator, N-1): 
    #print(o)
    num = num_lst[0]
    for i in range(1, len(num_lst)): 
        if o[i-1] == '+': 
            num += num_lst[i]
        elif o[i-1] == '*': 
            num *= num_lst[i]
        elif o[i-1] == '-': 
            num -= num_lst[i]
        elif o[i-1] == '/':
            if num < 0 and num_lst[i] > 0:
                num = -1*(num*(-1)//num_lst[i])
            else: 
                num = num//num_lst[i]
        #print(num)
    
    if max_ < num: 
        max_ = num
    if min_ > num: 
        min_ = num
print(max_, min_, sep='\n')