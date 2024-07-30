def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f'{h:02}:{m:02}:{s:02}'

current_time = input().strip()
start_time = input().strip()

current_seconds = time_to_seconds(current_time)
start_seconds = time_to_seconds(start_time)

if start_seconds >= current_seconds:
    remaining_seconds = start_seconds - current_seconds
else:
    remaining_seconds = (24 * 3600) - current_seconds + start_seconds

print(seconds_to_time(remaining_seconds))
