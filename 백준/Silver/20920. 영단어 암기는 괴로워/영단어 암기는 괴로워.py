from collections import defaultdict
import sys 

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(N): 
    lst.append(input().strip())  # 입력 시 strip()을 통해 '\n' 제거

word_cnt_dict = defaultdict(int)  # 0으로 초기화

for word in lst: 
    word_len = len(word)
    if word_len < M:   # 1. M개 이상 단어만 
        continue
    else: 
        word_cnt_dict[word] += 1

# 다중 정렬: 1. 빈도수 내림차순, 2. 길이 내림차순, 3. 알파벳 사전순
for key in sorted(word_cnt_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):  
    print(key[0])
