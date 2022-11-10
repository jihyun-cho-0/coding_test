"""1번째 시도 >>> 오답
def solution(participant, completion):

    sorted(participant)
    sorted(completion)
    
    for p in participant:
        if p not in completion:
            participant.remove(p)
    
    answer = participant
        
    return answer
"""

# def solution(participant, completion):
  
#     hash_table = list([0 for i in range(len(participant))])
#     print(hash_table)
#     temp = 0
#     print(temp)
#     for p in participant:
#         hash(p)
#         temp += int(hash(p))
#     print(temp)
#         key % 8

#     return 


from collections import defaultdict

def solution(participant, completion):
    answer = ""
    finish = defaultdict(list)

    for p in participant:
        finish[p].append(0)
 
    for c in completion:
        finish[c].pop()
        if len(finish[c]) >= 1:
            answer.append(c)
    
    return print(answer)



participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)