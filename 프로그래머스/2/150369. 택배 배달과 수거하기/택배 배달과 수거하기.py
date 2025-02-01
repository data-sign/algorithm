def solution(cap, n, deliveries, pickups):
    total_distance = 0
    current_delivery = 0
    current_pickup = 0

    for i in range(n - 1, -1, -1):
        current_delivery += deliveries[i]
        current_pickup += pickups[i]

        while current_delivery > 0 or current_pickup > 0:
            current_delivery -= cap
            current_pickup -= cap
            total_distance += (i + 1) * 2

    return total_distance
