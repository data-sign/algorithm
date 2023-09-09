from itertools import combinations


def find_intersection_point(line1, line2):  # 두 직선의 모든 좌표가 정수인 교점 구하기
    a, b, e = line1  # ax + by + e = 0
    c, d, f = line2  # cx + dy + f = 0
    if a * d == b * c:  # 기울기가 일치하거나 평행인 경우
        return
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    if x == int(x) and y == int(y):  # 교점이 정수라면
        return (int(x), int(y))


def solution(line):
    points = set()  # 교점
    x_points, y_points = set(), set()  # x_points : 교점의 x좌표들, y_points : 교점의 y좌표들
    for a, b in combinations(line, 2):  # 선분들 중 2개 골라서
        point = find_intersection_point(a, b)
        if point:  # 교점이 존재한다면
            points.add(point)
            x_points.add(point[0])
            y_points.add(point[1])

    x_min, x_max = min(x_points), max(x_points)  # 교점의 x좌표들 중 최소값과 최대값
    y_min, y_max = min(y_points), max(y_points)  # 교점의 y좌표들 중 최소값과 최대값

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in points:
        answer[y_max - y][x - x_min] = '*'  # 교점에 별 만들기
    return list(map(''.join, answer))