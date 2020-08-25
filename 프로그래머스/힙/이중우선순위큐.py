import heapq

def solution(operations):
    answer = [0,0]
    heap = []

    for op in operations:
        op, num = op.split(" ")

        if op == 'I':
            heapq.heappush(heap,int(num))
        elif op =='D' and heap:
            if int(num)>0:
                heapq._heapify_max(heap)
                heapq.heappop(heap)
                if heap:
                    heapq.heapify(heap)
            else:
                heapq.heappop(heap)
    
    if heap:
        return [max(heap), min(heap)]
    else:
        return answer