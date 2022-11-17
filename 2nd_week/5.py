"""1번째 시도
def solution(absolutes, signs):
    
    for i, a in enumerate(absolutes):
        if signs[i] == false:
            absolutes[i] = -a

    answer = sum(absolutes)

    return answer
"""


# 정답1
def solution(absolutes, signs):
    
    for i, a in enumerate(absolutes):
        if not signs[i]:
            absolutes[i] = -a

    answer = sum(absolutes)

    return answer


"""정답2
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
"""




