def solution(number, k):
    stack = []

    # 먼저 stack의 top이 새로 stack에 들어갈 숫자보다 작으면 제거
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    # 제거할 수가 남았을때 뒤에서부터 제거
    while k > 0:
        stack.pop()
        k -= 1

    answer = "".join(stack)

    return answer



# 테스트 1 〉	통과 (0.04ms, 10.6MB)
# 테스트 2 〉	통과 (0.05ms, 10.7MB)
# 테스트 3 〉	통과 (0.06ms, 10.7MB)
# 테스트 4 〉	통과 (0.14ms, 10.6MB)
# 테스트 5 〉	통과 (0.22ms, 10.7MB)
# 테스트 6 〉	통과 (3.01ms, 10.8MB)
# 테스트 7 〉	통과 (8.86ms, 10.9MB)
# 테스트 8 〉	통과 (17.24ms, 11.1MB)
# 테스트 9 〉	통과 (37.10ms, 13.7MB)
# 테스트 10 〉	통과 (96.81ms, 13.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.6MB)