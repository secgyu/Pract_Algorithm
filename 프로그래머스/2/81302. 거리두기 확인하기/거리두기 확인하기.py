# 각 대기실에서 거리두기를 지켰는지 확인하는 함수
def check_place(place):
    # 방향 설정: 상, 하, 좌, 우, 대각선 및 거리 2를 나타내는 방향들
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    extended_directions = [
        (-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)
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
                        # 사이에 파티션이 없으면 규칙 위반
                        if abs(dr) == 2 and place[(r + nr) // 2][c] != 'X':
                            return False
                        elif abs(dc) == 2 and place[r][(c + nc) // 2] != 'X':
                            return False
                        elif abs(dr) == 1 and abs(dc) == 1:
                            if place[r + dr][c] != 'X' or place[r][c + dc] != 'X':
                                return False
    return True

def solution(places):
    answer = []
    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer