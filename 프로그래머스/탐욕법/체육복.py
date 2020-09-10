def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 체육복을 가져왔고, 도난당한 학생
    dup = lost[:]
    for d in dup:
        if d in reserve:
            reserve.remove(d)
            lost.remove(d)
            answer += 1

    # 양쪽방향으로 여벌을 가지고 있는지 확인
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer += 1

    return answer

# 테스트 1 〉	통과 (0.04ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.8MB)
# 테스트 5 〉	통과 (0.04ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.7MB)
# 테스트 7 〉	통과 (0.05ms, 10.6MB)
# 테스트 8 〉	통과 (0.04ms, 10.6MB)
# 테스트 9 〉	통과 (0.04ms, 10.6MB)
# 테스트 10 〉	통과 (0.04ms, 10.6MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.7MB)