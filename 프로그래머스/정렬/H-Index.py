def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()

    # H-Index 찾기
    for idx, c in enumerate(citations):
        if n-idx >= c:
            answer = c

    return answer

