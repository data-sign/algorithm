N, L = map(int, input().split())
matrix = []
for _ in range(N): 
    matrix.append(list(map(int, input().split())))
    
def detect_road(road): 
    visited = [0]*N
    for i in range(len(road)-1):
        if len(set(road)) == 1: 
            return True
        # 안 되는 조건 2 이상 차이 
        if abs(road[i] - road[i+1]) > 1 : 
            return False 
        # 경사로 설치 조건 안 맞음 : 경사로 길이(L)만큼 칸의 높이가 1 차이 나는 칸이 있어야 함 
        if road[i] - road[i+1]== 1:    # 3->2
            for x in range(1, L+1):
                if (i+x>=N):
                    return False  
                elif (road[i] -1 != road[i+x])|(visited[i+x]==1):
                    return False
                else: 
                    visited[i+x] = 1

        if road[i+1] - road[i]== 1:   # 2->3
            for x in range(L):
                if (i-x<0): 
                    return False
                elif (road[i+1] -1 != road[i-x])|(visited[i-x]==1):  # 경사로 놓을 칸이 범위를 넘거나 1차이가 나지 않거나 방문했으면 
                    return False
                else: 
                    visited[i-x] = 1
                                   
    return True

cnt = 0
for i in range(N): 
    # 행
    if detect_road(matrix[i]): 
        cnt += 1

    # 열
    road = [matrix[j][i] for j in range(N)] 
    if detect_road(road): 
        cnt += 1
print(cnt)