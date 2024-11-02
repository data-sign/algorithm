## 백준 볼모으기 
# 무슨색으로 모을거냐? 
# 어느 방향으로 모을거냐? 왼쪽? 오른쪽? 
# 같은 색이 되도록 왼쪽 혹은 오른쪽으로 뭉치기 
# 뭉칠 때 뭉치는 기준 가까운 순으로 옮기기 
# -> 맨끝 뭉치는 기준 제외 나머지를 차례로 옮기는 것. 
# 맨끝 뭉치는 기준 재외 => strip
# 차례로 옮기기 => 뭉친 거 제외 나머지 개수 
n = int(input())
balls = input().strip()

try_lst = []

# 빨간색 기준 모으기 : 왼쪽으로
try_rl = balls.lstrip('R') 
try_lst.append(try_rl.count('R'))

# 빨간색 기준 모으기 : 오른쪽으로 
try_rr = balls.rstrip('R') 
try_lst.append(try_rr.count('R'))

# 파란색 기준 모으기 : 왼쪽으로 
try_bl = balls.lstrip('B') 
try_lst.append(try_bl.count('B'))

# 파란색 기준 모으기 : 오른쪽으로 
try_br = balls.rstrip('B') 
try_lst.append(try_br.count('B'))

print(min(try_lst))
