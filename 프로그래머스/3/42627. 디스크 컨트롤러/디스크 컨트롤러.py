import heapq

def solution(jobs):
    jobs.sort()
    current_time, total_wait_time, i = 0, 0, 0
    heap = []
    n = len(jobs)
    
    while i < n or heap:
        while i < n and jobs[i][0] <= current_time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            total_wait_time += current_time - request_time
        else:
            current_time = jobs[i][0]
    return total_wait_time // n