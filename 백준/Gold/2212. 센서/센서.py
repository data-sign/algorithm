n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

if k >= n:
    print(0)  # 모든 센서를 개별적으로 분리할 수 있는 경우, 수신 범위는 0
else:
    sensor.sort()
    distance = [sensor[i+1] - sensor[i] for i in range(len(sensor) - 1)]
    
    # 가장 큰 거리 k-1개를 제거
    for i in range(k - 1):
        distance.remove(max(distance))
    
    # 남은 거리의 합이 최소 수신 범위가 됨
    print(sum(distance))
