def binary_search(low, high, times, n):
    if low > high:
        return high + 1
    mid = (low + high) // 2
    people = 0

    # 몇명까지 심사할 수 있는지 계산
    for t in times:
        people += mid // t

    if n == people:
        # 최솟값을 찾아야 하므로 1초 단축한 시간도 확인
        return min(mid, binary_search(low, mid - 1, times, n))
    elif n < people:
        return binary_search(low, mid - 1, times, n)
    else:
        return binary_search(mid + 1, high, times, n)


def solution(n, times):
    answer = binary_search(0, n * max(times), times, n)

    return answer

# 테스트 1 〉	통과 (0.04ms, 10.8MB)
# 테스트 2 〉	통과 (0.14ms, 10.8MB)
# 테스트 3 〉	통과 (3.75ms, 10.9MB)
# 테스트 4 〉	통과 (284.71ms, 83.7MB)
# 테스트 5 〉	통과 (413.46ms, 83.7MB)
# 테스트 6 〉	통과 (273.50ms, 83MB)
# 테스트 7 〉	통과 (515.74ms, 83.8MB)
# 테스트 8 〉	통과 (523.54ms, 83.7MB)
# 테스트 9 〉	통과 (0.08ms, 10.8MB)