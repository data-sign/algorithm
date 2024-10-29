X, Y = map(int, input().split())
current_win_rate = (Y * 100) // X  # 현재 승률

# 승률이 변하지 않는 경우
if current_win_rate >= 99:
    print(-1)
    exit()

# 이진 탐색을 위한 초기 설정
min_games = 0
max_games = 10**9  # 충분히 큰 수로 설정
result = -1

while min_games <= max_games:
    mid_games = (min_games + max_games) // 2
    new_wins = Y + mid_games
    new_games = X + mid_games
    new_win_rate = (new_wins * 100) // new_games

    if new_win_rate > current_win_rate:
        result = mid_games  # 승률이 변하는 경우
        max_games = mid_games - 1  # 더 적은 게임 수를 시도
    else:
        min_games = mid_games + 1  # 더 많은 게임 수를 시도

print(result)