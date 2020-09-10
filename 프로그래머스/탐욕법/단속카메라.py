def solution(routes):
    answer = 0
    # 차량이 고속도로에서 나가는 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    while routes:
        route = routes.pop(0)

        for r in routes[:]:
            # 중복되는 지점 찾기
            if r[0] <= route[1] <= r[1]:
                routes.remove(r)

        answer += 1

    return answer



# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 9.57MB)
# 테스트 2 〉	통과 (0.08ms, 9.63MB)
# 테스트 3 〉	통과 (0.10ms, 9.55MB)
# 테스트 4 〉	통과 (0.11ms, 9.7MB)
# 테스트 5 〉	통과 (0.11ms, 9.54MB)
#
# 효율성  테스트
# 테스트 1 〉	통과 (12.05ms, 9.77MB)
# 테스트 2 〉	통과 (4.89ms, 9.73MB)
# 테스트 3 〉	통과 (45.51ms, 9.94MB)
# 테스트 4 〉	통과 (0.34ms, 9.54MB)
# 테스트 5 〉	통과 (61.72ms, 9.98MB)