def solution(n):
    string = [x for x in str(n)]
    string.sort(reverse=True)

    answer = ""

    for s in string:
        answer += s

    return int(answer)