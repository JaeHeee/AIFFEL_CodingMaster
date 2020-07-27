T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    count = 0
    pos = 0

    while pos < N:
        for j in range(K, 0, -1):
            # 종점에 도착하면 종료
            if pos+j == N:
                pos = N
                break

            # 충전할 수 있는 경우
            if pos+j in charge:
                pos += j
                count += 1
                break
            # 충전할 수 없는 경우
            elif pos+j not in charge and j == 1:
                count = 0
                pos = N
                break

    print("#{} {}".format(i+1, count))