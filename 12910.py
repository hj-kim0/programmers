def solution(arr, divisor):
    answer = []
    arr = sorted(list(arr))
    
    for _ in range(len(arr)):
        if arr[_]%divisor == 0:
            answer.append(arr[_])
            
    if(len(answer) == 0):
        answer.append(-1)
    
    return answer
