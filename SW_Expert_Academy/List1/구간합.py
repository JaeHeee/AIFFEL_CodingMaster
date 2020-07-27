T = int(input(''))

for i in range(T):
    sum_ = []
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # SUM
    for j in range(0, N-M+1):
        temp = 0
        for k in range(j,j+M):
            temp += numbers[k]
        sum_.append(temp)
    
    print("#{} {}".format(i+1, max(sum_)-min(sum_)))