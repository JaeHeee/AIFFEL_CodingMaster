def solution(numbers, target):
    node = [0]
    # 숫자를 하나씩 가져와서 +,- 하는 경우를 계산해서 추가합니다.
    for n in numbers:
        child = []
        for i in node:
            child.append(i + n)
            child.append(i - n)
        node = child

    return node.count(target)



# 테스트 1 〉	통과 (174.04ms, 50.5MB)
# 테스트 2 〉	통과 (174.97ms, 48.9MB)
# 테스트 3 〉	통과 (0.73ms, 9.57MB)
# 테스트 4 〉	통과 (1.07ms, 9.61MB)
# 테스트 5 〉	통과 (6.03ms, 10.5MB)
# 테스트 6 〉	통과 (0.56ms, 9.45MB)
# 테스트 7 〉	통과 (0.28ms, 9.42MB)
# 테스트 8 〉	통과 (1.83ms, 9.77MB)