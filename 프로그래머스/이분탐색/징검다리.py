def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    # 각 바위 사이의 거리
    dist = [rocks[0]]
    for i in range(1,len(rocks)):
        dist.append(rocks[i]-rocks[i-1])

    min_ = 0
    max_ = distance

    while min_ <= max_:
        mid = (max_ + min_) // 2
        count = 0
        min_dist = 1e9
        temp = dist[:]

        for j in range(len(temp)):
            if temp[j] < mid:
                count += 1
                # 마지막이 아닌 경우
                if j != len(temp)-1:
                    temp[j+1] += temp[j]
            else:
                min_dist = min(min_dist, temp[j])

        if count > n:
            max_ = mid - 1
        else:
            min_ = mid + 1
            answer = min_dist

    return answer

# 테스트 1 〉	통과 (1.10ms, 9.57MB)
# 테스트 2 〉	통과 (1.01ms, 9.55MB)
# 테스트 3 〉	통과 (1.07ms, 9.63MB)
# 테스트 4 〉	통과 (33.67ms, 10MB)
# 테스트 5 〉	통과 (31.69ms, 10.1MB)
# 테스트 6 〉	통과 (315.60ms, 14MB)
# 테스트 7 〉	통과 (396.75ms, 16MB)
# 테스트 8 〉	통과 (412.46ms, 16MB)
# 테스트 9 〉	통과 (0.02ms, 9.47MB)