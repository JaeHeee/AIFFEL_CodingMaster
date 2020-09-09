from collections import defaultdict

# bfs 이용해서 노드별 최단경로 저장
def bfs(start, graph):
    queue = []
    queue.append(start)
    checked = [0] * len(graph)
    path_length = [0] * len(graph) # 최단경로
    checked[0] = True

    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if checked[n - 1] == 0:
                queue.append(n)
                checked[n - 1] = True
                path_length[n - 1] = path_length[node - 1] + 1

    return path_length


def solution(n, edge):
    graph = defaultdict(list)

    # 그래프 만들기
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    path_length = bfs(1, graph)

    if max(path_length):
        answer = path_length.count(max(path_length))
        return answer
    else:
        return 0


# 테스트 1 〉	통과 (0.05ms, 10.7MB)
# 테스트 2 〉	통과 (0.06ms, 10.7MB)
# 테스트 3 〉	통과 (0.12ms, 10.7MB)
# 테스트 4 〉	통과 (0.32ms, 10.8MB)
# 테스트 5 〉	통과 (1.19ms, 12MB)
# 테스트 6 〉	통과 (2.92ms, 19.1MB)
# 테스트 7 〉	통과 (36.86ms, 88.9MB)
# 테스트 8 〉	통과 (58.03ms, 125MB)
# 테스트 9 〉	통과 (70.76ms, 125MB)