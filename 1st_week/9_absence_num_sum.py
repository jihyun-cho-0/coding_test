def solution(numbers):
   
    zero_to_nine = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    absence_num = zero_to_nine - set(numbers)
    answer = sum(absence_num)
    return answer