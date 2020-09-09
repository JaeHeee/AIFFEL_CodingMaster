def count(word, target):
    num = 0
    for idx, w in enumerate(word):
        if w != target[idx]:
            num += 1
    return num


def bfs(begin, target, words, visited, answer):
    queue = []
    queue.append(begin)
    while queue:
        word = queue.pop()

        if word == target:
            return answer

        for i in range(0, len(words)):
            # 글자수가 하나만 다른 단어 찾기
            if count(words[i], word) == 1:
                if visited[i] == 1:
                    continue
                visited[i] = 1
                queue.append(words[i])
        answer += 1


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [0] * len(words)

    answer = bfs(begin, target, words, visited, answer)

    return answer


# 테스트 1 〉	통과 (0.01ms, 9.43MB)
# 테스트 2 〉	통과 (0.10ms, 9.5MB)
# 테스트 3 〉	통과 (0.79ms, 9.54MB)
# 테스트 4 〉	통과 (0.02ms, 9.51MB)
# 테스트 5 〉	통과 (0.00ms, 9.51MB)