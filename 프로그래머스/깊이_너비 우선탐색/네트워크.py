def dfs(computers, visited, start):
    if visited[start]:
        return
    visited[start] = 1
    for idx, c in enumerate(computers[start]):
        # 연결되어 있다면 visit
        if c == 1:
            dfs(computers, visited, idx)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    return answer




# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.07ms, 10.8MB)
# 테스트 4 〉	통과 (0.07ms, 10.8MB)
# 테스트 5 〉	통과 (0.03ms, 10.7MB)
# 테스트 6 〉	통과 (0.17ms, 10.9MB)
# 테스트 7 〉	통과 (0.05ms, 10.7MB)
# 테스트 8 〉	통과 (0.13ms, 10.8MB)
# 테스트 9 〉	통과 (0.09ms, 10.8MB)
# 테스트 10 〉	통과 (0.10ms, 10.8MB)
# 테스트 11 〉	통과 (0.46ms, 14MB)
# 테스트 12 〉	통과 (0.36ms, 12.8MB)
# 테스트 13 〉	통과 (0.24ms, 10.9MB)