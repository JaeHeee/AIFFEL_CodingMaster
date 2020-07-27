T = int(input(''))

for i in range(T):
    N = int(input(''))
    
    # 숫자들을 입력받고 정렬
    numbers = list(map(int,input().split()))
    numbers.sort()

    print("#{} {}".format(i+1, (numbers[-1] - numbers[0])))