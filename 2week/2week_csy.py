def solution(scores):
    answer = ''

    for j in range(len(scores)):
        cnt = len(scores) # 학생 수
        score = 0
        high = 0 # 최댓값/최솟값 지정
        low = 101

        for i in range(len(scores)):
            score += scores[i][j]
            if i == j: # 스스로 평가한 점수이므로 continue로 최소값/최대값 구하는 곳에서는 패스
                continue
            if high < scores[i][j]: # 반복문 사용해서 최댓값/최솟값 돌리기
                high = scores[i][j]
            elif low > scores[i][j]:
                low = scores[i][j]

        if scores[j][j] > high or scores[j][j] < low: # 스스로 평가한 점수가 최댓값/최솟값인 경우
            score -= scores[j][j]
            cnt -= 1
        avg = score / cnt

        if avg >= 90:
            answer = answer + 'A'
        elif avg >= 80:
            answer = answer + 'B'
        elif avg >= 70:
            answer = answer + 'C'
        elif avg >= 50:
            answer = answer + 'D'
        else:
            answer = answer + 'F'

    return answer
