def solution(n):
    # 숫자를 넣어줄 배열 초기화. n*n으로 만들 필요는 없음
    lst=[[0]*n for _ in range(n)]
    # x,y축 방향이동용 리스트
    dx=[1,0,-1]
    dy=[0,1,-1]
    i=0
    num=1
    x=y=0
    answer=[]
    while n>0:    
        for j in range(n):
            lst[x][y]=num
            num+=1
            # n-1을 포함시키면 x,y가 범위를 벗어난다.
            if j<n-1:
                x=x+dx[i]
                y=y+dy[i]
            # n-1번째가 되면 방향 전환
            else:
                # 이전 반복문에서 방향이동용 리스트가 마지막이었으면 0번째로 초기화
                if i==2:
                    i=0
                    x=x+dx[i]
                    y=y+dy[i]
                else:
                    i+=1
                    x=x+dx[i]
                    y=y+dy[i]

        n-=1
    for a in range(len(lst)):
        for b in range(len(lst)):
            if lst[a][b]!=0:
                answer.append(lst[a][b])
    return answer


print(solution(5))