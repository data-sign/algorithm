## 9095 : 1,2,3 더하기 
# 1) n-1 번째 나열된 숫자 조합 뒤에 +1 붙이기 -> lst[i-1]
# 2) n-2 번째 나열된 숫자 조합 뒤에 +2 붙이기 -> lst[i-2]
# 3) n-3 번째 나열된 숫자 조합 뒤에 +3 붙이기 -> lst[i-3]
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T): 
    n = int(input())
    lst = [1, 2, 4]
    for i in range(3, n):
        result = lst[i-1] + lst[i-2] + lst[i-3]
        lst.append(result)
        # print(i, lst)
    print(lst[n-1])