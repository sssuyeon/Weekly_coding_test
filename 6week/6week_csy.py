# 각 복서들의 정보를 info 리스트에 저장
# 각 정보를 승률, 무거운 복서를 이긴 횟수, 몸무게, 번호 순으로 정렬 (번호만 오름차순 정렬/나머지는 내림차순 정렬)
# 정렬된 결과에서 (번호+1) return (인덱스는 0부터 시작)

def solution(weights, head2head):
    info = []
    n = len(weights) # 종 인원수
    
    for i in range(n):
        cnt = [0, 0, 0] # (총 횟수, 이긴 횟수, 자신보다 무거운 복서를 이긴 횟수) 나타내는 리스트
        for j in range(n):
            if head2head[i][j] == "N":
                continue
            if head2head[i][j] == "W":
                cnt[1] += 1; # 이긴 횟수에 1씩 더하기
                cnt[2] += weights[i] < weights[j] # 자신보다 무거운 복서를 이긴 횟수에 1씩 더하기
            cnt[0] += 1 # 총 횟수(이긴 횟수+진 횟수)에 1씩 더하기
        
        # 승률계산
        if cnt[1] == 0:
            win_rate = 0
        else:
            win_rate = cnt[1] / cnt[0]
        
        # 승률, 무거운 복서 이긴 횟수, 몸무게, 번호 순서대로
        info.append([-win_rate, -cnt[2], -weights[i], i+1])
        
    # 정렬 후 번호만 answer에 저장
    info.sort()
    answer = [x[-1] for x in info]
    return answer
