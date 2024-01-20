# 리프노드는 간선 수가 하나 = input에서 한 번만 적힘 
from collections import defaultdict
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
node_lst = []
Tree = defaultdict(int)
for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a] += 1
    Tree[b] += 1

# 리프노드 세기 
leaf_node_cnt = 0
for i in range(2, N+1): 
    if Tree[i] == 1: 
        leaf_node_cnt += 1
        
print("%.3f"%(W/leaf_node_cnt))