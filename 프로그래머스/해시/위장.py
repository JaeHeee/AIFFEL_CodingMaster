def solution(clothes):
    answer = 1
    clothes_d = {}

    for c in clothes:
        if c[1] in clothes_d.keys():
            clothes_d[c[1]].append(c[0])
        else:
            clothes_d[c[1]] = [c[0]]

    for v in clothes_d.values():
        answer *= (len(v)+1)

    return answer - 1