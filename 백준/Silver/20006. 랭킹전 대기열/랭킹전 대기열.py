p, m = map(int, input().split())

room_lst = []
for _ in range(p):
    lv, id = input().split()
    lv = int(lv)

    joined = False
    for room in room_lst:
        if (len(room) < m) and (room[0][0] - 10 <= lv <= room[0][0] + 10):
            room.append((lv, id))
            joined = True
            break
    
    if not joined:
        room_lst.append([(lv, id)])

# 결과 출력
for room in room_lst:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for member in sorted(room, key=lambda x: x[1]):
        print(member[0], member[1])