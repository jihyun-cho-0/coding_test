
""" 1번째 시도 >>> 테스트 결과 2개 중 1개 성공
def solution(n, lost, reserve):
   
    have_clothes = n - len(lost)

    lend = []
    for i in reserve:
        pre = i - 1
        post = i + 1
        lend.append(pre)
        lend.append(post)

    borrowed = set(lend) & set(lost)

    answer = have_clothes + len(borrowed)
    return answer
"""

""" 2번째 시도 >>> 테스트 결과 2개 중 1개 성공
def solution(n, lost, reserve):
   
    have_clothes = n - len(lost)

    possible = []
    for i in lost:
        pre = i - 1
        post = i + 1
        possible.append(pre)
        possible.append(post)

    borrowed = set(possible) & set(reserve)

    answer = have_clothes + len(borrowed)
    return answer
"""

def solution(n, lost, reserve):
   
    have_clothes = n - len(lost)
    print(f"have_clothes : {have_clothes}")

    possible = []
    for i in lost:
        pre = i - 1
        post = i + 1
        possible.append(pre)
        possible.append(post)
    print(f"possible : {possible}")

    borrowed = set(possible) & set(reserve)
    print(f"set(possible) : {set(possible)}")
    print(f"set(reserve) : {set(reserve)}")
    print(f"borrowed : {borrowed}")

    answer = have_clothes + len(borrowed)
    print(f"answer : {answer}")
    return answer



n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))