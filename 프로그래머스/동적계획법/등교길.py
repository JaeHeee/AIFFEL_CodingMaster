def solution(m, n, puddles):
    answer = 0

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # 잠긴구역인지 확인
            if [j + 1, i + 1] in puddles:
                dp[i][j] = 0
            # 집인 경우
            elif i == 0 and j == 0:
                dp[i][j] = 1
            # 이 지점에 도달할 수 있는 방법의 수 계산
            else:
                if i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    answer = dp[-1][-1]

    return answer % 1000000007


#
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 9.66MB)
# 테스트 2 〉	통과 (0.02ms, 9.67MB)
# 테스트 3 〉	통과 (0.04ms, 9.64MB)
# 테스트 4 〉	통과 (0.06ms, 9.68MB)
# 테스트 5 〉	통과 (0.10ms, 9.66MB)
# 테스트 6 〉	통과 (0.10ms, 9.67MB)
# 테스트 7 〉	통과 (0.06ms, 9.7MB)
# 테스트 8 〉	통과 (0.20ms, 9.67MB)
# 테스트 9 〉	통과 (0.09ms, 9.68MB)
# 테스트 10 〉	통과 (0.04ms, 9.6MB)

# 효율성  테스트
# 테스트 1 〉	통과 (4.84ms, 9.8MB)
# 테스트 2 〉	통과 (1.52ms, 9.72MB)
# 테스트 3 〉	통과 (1.81ms, 9.71MB)
# 테스트 4 〉	통과 (2.58ms, 9.84MB)
# 테스트 5 〉	통과 (1.95ms, 9.76MB)
# 테스트 6 〉	통과 (3.83ms, 9.82MB)
# 테스트 7 〉	통과 (1.90ms, 9.86MB)
# 테스트 8 〉	통과 (3.27ms, 9.85MB)
# 테스트 9 〉	통과 (3.34ms, 9.88MB)
# 테스트 10 〉	통과 (2.45ms, 9.91MB)