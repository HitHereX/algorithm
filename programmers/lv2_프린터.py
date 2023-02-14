from collections import deque

def solution(priorities, location):    
    priorities = deque(enumerate(priorities))
    reps = 0
    while True:
        maxnum = max([pair[1] for pair in priorities])
        temp = priorities.popleft()
#        temp[0] == index, temp[1] == index's priority
        if temp[1] == maxnum:
            reps += 1
            if temp[0] == location:
                break
        else:
            priorities.append(temp)
    
    return reps
    
    
 ##THINKFLOW
 #1. enumerate를 사용하여 초기 큐 내용에 인덱스 매핑
 #2. while로 돌면서 queue.popleft해서 맨 앞 값을 temp에 임시저장
 #  2-1.queue 내에 temp 보다 더 높은 값이 있는 경우 = 출력불가 → temp를 다시  append
 #  2-2.아닌 경우 = 출력하는 경우
 #   → rep += 1로 횟수 올리고
 #   만약 그 뽑은 값이 타겟값(location)이었다면 반복종료 및 답 리턴
 
 ##LEARNED:
 # maxnum을 분기 전에 빼놓지 않으면 체크하고자 하는 최대 수가 큐에 들어있지 않기 때문에 의도와 분기문이 다르게 흘러간다
