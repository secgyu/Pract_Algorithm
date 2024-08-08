S, T, D = map(int, input().split())

time_to_meet = D / (2 * S)

distance_flown = time_to_meet * T

print(int(distance_flown))
