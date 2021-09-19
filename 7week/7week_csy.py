def solution(enter, leave):
    answer = [0 for _ in range(len(enter)+1)] # 각 인덱스가 몇 명 만났는지 (숫자 0은 사용하지 않으므로 len(enter)+1 만큼 0으로 초기화)
    room = [] # 회의실
    
    for i in enter:
        for r in room:
            answer[r] += 1 # i 인덱스 사람 입장했을 때 회의실에 있던 r 인덱스 사람은 +1
        answer[i] += len(room) # i 인덱스 사람은 회의실에 있던 사람들 모두와 만났으므로 +len(room)
        room.append(i)
        
        while leave and leave[0] in room: # leave[0] 가 room에 있다면 떠나야 하므로 room에서 제거해줌
            room.remove(leave.pop(0))
            
    return answer[1:] # answer[0]은 사용하지 않았음으로 answer[1:]
