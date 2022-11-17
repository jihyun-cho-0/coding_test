def solution(a, b):
    if a<b:
        start = a
        stop = b
    else:
        start = b
        stop = a
        
    between = [x for x in range(start, stop+1)]
    answer = sum(between)
    
    return answer