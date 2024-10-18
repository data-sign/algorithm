## 백준 22233 : 가희와 키워드 
# 메모장에 있는 키워드 중 블로그 글에 쓴 키워드 삭제 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = set()
for _ in range(N):
    memo.add(input().strip())


for _ in range(M):
    keyword = input().split(',')

    for kw in keyword:
        memo.discard(kw.strip())
    # print(memo)
    print(len(memo))
