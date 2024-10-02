def solution(record):
    user = {}
    log = []

    for i in record:
        info = i.split()
        action = info[0]
        user_id = info[1]

        if action == "Enter":
            name = info[2]
            user[user_id] = name
            log.append((user_id, "님이 들어왔습니다."))
        elif action == "Leave":
            log.append((user_id, "님이 나갔습니다."))
        elif action == "Change":
            name = info[2]
            user[user_id] = name
    
    answer = [user[user_id] + action for user_id,action in log]
    return answer