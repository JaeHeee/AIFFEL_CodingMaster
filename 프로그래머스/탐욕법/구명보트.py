def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1

    # 제일 무거운 사람부터 구출
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer


# 정확성  테스트
# 테스트 1 〉	통과 (1.08ms, 9.71MB)
# 테스트 2 〉	통과 (1.02ms, 9.59MB)
# 테스트 3 〉	통과 (1.01ms, 9.71MB)
# 테스트 4 〉	통과 (0.91ms, 9.59MB)
# 테스트 5 〉	통과 (0.51ms, 9.52MB)
# 테스트 6 〉	통과 (0.30ms, 9.41MB)
# 테스트 7 〉	통과 (0.86ms, 9.59MB)
# 테스트 8 〉	통과 (0.05ms, 9.52MB)
# 테스트 9 〉	통과 (0.07ms, 9.52MB)
# 테스트 10 〉	통과 (2.03ms, 9.53MB)
# 테스트 11 〉	통과 (0.78ms, 9.54MB)
# 테스트 12 〉	통과 (0.71ms, 9.59MB)
# 테스트 13 〉	통과 (0.91ms, 9.54MB)
# 테스트 14 〉	통과 (1.09ms, 9.53MB)
# 테스트 15 〉	통과 (0.67ms, 9.6MB)
#
#
# 효율성  테스트
# 테스트 1 〉	통과 (9.52ms, 9.95MB)
# 테스트 2 〉	통과 (10.48ms, 9.94MB)
# 테스트 3 〉	통과 (8.89ms, 9.97MB)
# 테스트 4 〉	통과 (9.70ms, 10MB)
# 테스트 5 〉	통과 (8.73ms, 9.97MB)