def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr.pop(0))
    while arr:
        if answer[-1] != arr[0]:
            answer.append(arr.pop(0))
    return answer