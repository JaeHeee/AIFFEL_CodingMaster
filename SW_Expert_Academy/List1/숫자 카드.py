T = int(input(''))

for i in range(T):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    idx = 0
    N = int(input(''))
    # 숫자를 입력받아서 리스트로 만들어준다.
    numbers = list(input(''))

    # count list에 해당하는 숫자의 갯수를 올려준다.
    for n in numbers:
        counts[int(n)] += 1

    for j in range(9,-1,-1):
        if max(counts) == counts[j]:
            idx = j
            break
    
    print("#{} {} {}".format(i+1, idx, max(counts)))
