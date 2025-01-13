def solution(board, skill):
    m, n = len(board), len(board[0])  # 행, 열 크기
    impact = [[0] * (n + 1) for _ in range(m + 1)]  # 누적합을 저장할 배열

    # skill 정보를 누적합 배열에 반영
    for type_, r1, c1, r2, c2, degree in skill:
        degree = -degree if type_ == 1 else degree  # 공격은 음수, 회복은 양수
        impact[r1][c1] += degree
        impact[r1][c2 + 1] -= degree
        impact[r2 + 1][c1] -= degree
        impact[r2 + 1][c2 + 1] += degree

    # 누적합 계산 (위 -> 아래)
    for i in range(m):
        for j in range(n):
            impact[i][j + 1] += impact[i][j]

    # 누적합 계산 (왼쪽 -> 오른쪽)
    for j in range(n):
        for i in range(m):
            impact[i + 1][j] += impact[i][j]

    # 원래 board 값에 누적합을 적용하여 최종 값 계산
    answer = 0
    for i in range(m):
        for j in range(n):
            board[i][j] += impact[i][j]
            if board[i][j] > 0:  # 건물이 아직 남아있는 경우
                answer += 1

    return answer
