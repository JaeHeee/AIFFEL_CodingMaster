def solution(n, costs):
    answer = 0
    island = set()
    count = 1

    # cost가 작은 순서대로 정렬
    costs.sort(key=lambda x: x[2])
    island.add(costs[0][0])

    while len(island) != n:
        for c in costs:
            # 하나라도 있어야 연결가능
            if c[0] in island or c[1] in island:
                island.add(c[0])
                island.add(c[1])
                # len(island) == count 이면 이미 연결된 상황
                if len(island) > count:
                    count = len(island)
                    answer += c[2]
                    break

    return answer


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 9.65MB)
# 테스트 2 〉	통과 (0.01ms, 9.7MB)
# 테스트 3 〉	통과 (0.02ms, 9.66MB)
# 테스트 4 〉	통과 (0.05ms, 9.59MB)
# 테스트 5 〉	통과 (0.02ms, 9.64MB)
# 테스트 6 〉	통과 (0.05ms, 9.58MB)
# 테스트 7 〉	통과 (0.07ms, 9.55MB)
# 테스트 8 〉	통과 (0.02ms, 9.64MB)