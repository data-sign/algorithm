def solution(places):
    
    # (1) p의 위치 반환
    def fn_p_location(place): 
        location = []
        for i in range(5): 
            for j in range(5): 
                if place[i][j] == 'P': 
                    location.append((i, j))
        return location


    # (2) P의 거리 계산 
    def fn_distance(location): 
        for i in range(len(location)): 
            for j in range(i+1, len(location)): 

                (x1, y1), (x2, y2) = location[i], location[j]
                distance = abs(x1-x2) + abs(y1-y2)
                if distance == 1: 
                    return 0

                if distance <= 2: 
                    # (3) P 사이의 X 확인 : 좌표 차이 
                    if x1 == x2: 
                        if place[x1][y1+1] == 'O': 
                            return 0
                    elif y1 == y2: 
                        if place[x1+1][y1] == 'O': 
                            return 0
                    else: 
                        if (place[x1][y2]=='O')|(place[x2][y1]=='O'):
                            return 0
        return 1
    
    answer = []
    for place in places: 
        location = fn_p_location(place)
        answer.append(fn_distance(location))
    return answer