def solution(answers):

    answer = []

    rule_1 = [1, 2, 3, 4, 5]
    rule_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    rule_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
 
    all_score = [0, 0, 0]

    for i in range(len(answers)):

        if answers[i] == rule_1[i % len(rule_1)]:
            all_score[0] += 1

        if answers[i] == rule_2[i % len(rule_2)]:
            all_score[1] += 1

        if answers[i] == rule_3[i % len(rule_3)]:
            all_score[2] += 1

    max_score = max(all_score)

    for i in range(len(all_score)):

        if all_score[i] == max_score:
            answer.append(i+1)

    return answer