# 17144번 미세먼지 안녕!

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board, cleaner = [], []

for i in range(r):
    board.append(list(map(int, input().split())))
    for j in range(len(board[i])):
        # 공기청정기 위치 받기
        if board[i][j] == -1:
            cleaner.append((i, j))


# 미세먼지 확산 함수 생성
def dust_diffusion():
    # 상, 하, 좌, 우 방향 표시
    steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 각 위치마다 확산되는 미세먼지 양 표시
    diffusion = [[0] * c for _ in range(r)]
    # 확산
    for i in range(r):
        for j in range(c):
            if not (board[i][j] == 0 or board[i][j] == -1):
                turn = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in cleaner:
                        turn += 1
                        diffusion[nx][ny] += board[i][j] // 5
                board[i][j] = board[i][j] - (board[i][j] // 5 * turn)
    # 남은 미세먼지 양 계산
    for i in range(r):
        for j in range(c):
            board[i][j] += diffusion[i][j]
    return

# 공기청정기 바람 방향이 반시계 방향으로 이동
def dust_clean_up():
    # 동, 북, 서, 남 방향
    up_step = [[0, 1], [-1, -0], [0, -1], [1, 0]]
    # 방향 바꾸기
    direct = 0
    # 공기청정기 위쪽 위치
    x, y = cleaner[0]
    # 시작 위치 행 좌표
    up, y = x, 1
    # 이전 값
    previous = 0
    while True:
        # 이동 위치 확인
        nx, ny = x + up_step[direct][0], y + up_step[direct][1]
        # 처음 위치로 되돌아오면 종료
        if x == up and y == 0:
            break
        # 맵을 벗어나는 곳이라면
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            # 방향 바꾸고 건너뛰기
            direct += 1
            continue
        # 두 변수 값 바꾸기(swap)
        board[x][y], previous = previous, board[x][y]
        # 다음 위치로 이동
        x, y = nx, ny
    return

# 공기청정기 바람 방향이 시계 방향으로 이동
def dust_clean_down():
    # 동, 남, 서, 북 방향
    down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 방향 바꾸기
    direct = 0
    # 공기청정기 아래쪽 위치
    x, y = cleaner[1]
    # 시작 위치 행 좌표
    down, y = x, 1
    # 이전 값
    previous = 0
    while True:
        # 이동 위치 확인
        nx, ny = x + down_step[direct][0], y + down_step[direct][1]
        # 처음 위치로 되돌아오면 종료
        if x == down and y == 0:
            break
        # 맵을 벗어나는 곳이라면
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            # 방향 바꾸고 다음 코드부터 건너뛰기
            direct += 1
            continue
        # 두 변수 값 바꾸기(swap)
        board[x][y], previous = previous, board[x][y]
        # 다음 위치로 이동
        x, y = nx, ny
    return

# T초 후까지 반복
for _ in range(t):
    dust_diffusion()
    dust_clean_up()
    dust_clean_down()

# T초 후에 남아있는 미세먼지의 양 총합 계산
ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            ans += board[i][j]

# 답 출력
print(ans)