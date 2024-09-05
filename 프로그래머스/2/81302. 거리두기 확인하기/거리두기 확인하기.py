# 각 대기실에서 거리두기를 지켰는지 확인하는 함수
def check_place(place):
    # 방향 설정: 상, 하, 좌, 우 (거리 1을 확인하기 위한 방향)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 거리 2를 확인하기 위한 확장된 방향 설정
    extended_directions = [
        (-2, 0), (2, 0), (0, -2), (0, 2),  # 세로/가로 거리 2
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # 대각선
    ]
    
    # 대기실 순회
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':  # 응시자가 앉아 있는 경우
                # 거리 1 확인 (바로 옆에 응시자가 있는지)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        return False
                
                # 거리 2 확인 (빈 테이블을 사이에 두고 응시자가 있는지)
                for dr, dc in extended_directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        # 세로, 가로 거리 2 확인
                        if abs(dr) == 2 and place[(r + nr) // 2][c] != 'X':
                            return False
                        elif abs(dc) == 2 and place[r][(c + nc) // 2] != 'X':
                            return False
                        # 대각선 거리 2 확인
                        elif abs(dr) == 1 and abs(dc) == 1:
                            if place[r + dr][c] != 'X' or place[r][c + dc] != 'X':
                                return False
    return True

# 전체 대기실 확인
def solution(places):
    answer = []
    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
