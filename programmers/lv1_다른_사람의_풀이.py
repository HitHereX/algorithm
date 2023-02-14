def solution(s, skip, index):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    DOCU = ''

    for i in ALPHABET:
        if i not in skip: 
            DOCU += i            

    answer = ''

    for char in s:
        char_idx = 0
        for j in range(len(DOCU)):
            if char == DOCU[j]:
                char_idx = j
                break
                
        answer += DOCU[(char_idx+index)%len(DOCU)]

    return answer
