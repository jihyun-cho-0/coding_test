def solution(sizes):

    width = []
    height = []

    for i in sizes:

        if i[1] < i[0]:
            i.reverse()

        width.append(i[0])
        height.append(i[1])

    max_width = max(width)
    height_width = max(height)
    answer = max_width * height_width

    return answer