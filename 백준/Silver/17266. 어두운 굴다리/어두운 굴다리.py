import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))

# 이진 탐색을 통해 최소 h를 찾기
def can_light(h):
    tunnel = [0] * (n + 1)  # 구간 업데이트를 위한 배열 (끝에 하나 더 추가)
    
    for i in range(m):
        start = max(0, lst[i] - h)
        end = min(n, lst[i] + h)
        # 구간을 밝히는 방식으로 업데이트
        tunnel[start] += 1
        if end < n:
            tunnel[end] -= 1
    
    # 구간을 누적해서 계산 (슬라이딩 윈도우 방식)
    lighted = 0
    for i in range(n):
        lighted += tunnel[i]
        if lighted == 0:
            return False  # 한 구간이라도 불이 안 켜지면 False
    
    return True  # 모든 구간이 밝혀졌으면 True

# 이진 탐색으로 h의 값을 찾기
left, right = 0, n  # h의 범위는 0부터 n까지
answer = n

while left <= right:
    mid = (left + right) // 2
    if can_light(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
