import heapq

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
#매트릭스를 90% 회전시켜주는 코드
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i -1] = a[i][j]
    return result

#또는 
board = list(map(list, zip(*board[::-1])))


# 전체돌면서 확인
def check(new_lock):
    lock_length = len(new_lock) //3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

#숫자가 소수인지 알고리즘
def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True
#문자가 알파벳인지
string = "???"
if string.isalpha():
    print("yes")




#방향확인시
#     상  우  하  좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#중복순열
from itertools import product
n = 4
print(list(product(['+','-','*','/'], repeat=(n-1))))


from bisect import bisect_left, bisect_right

def count_range(array,x,y):
    right = bisect_right(array,y)
    left = bisect_left(array,x)
    return right - left


def frequent_sort(data):
    #rt_data = set()
    rt_data =Counter(data).most_common()
    return rt_data

from collections import OrderedDict

fishes =OrderedDict(sorted(fishes.items(), key=lambda t: t[0]))


#2중미로 최단거리

def bfs():
    t_dist = [[-1]*n for _ in range(n)]
    tempq= deque([(s_pos[0],s_pos[1])])
    t_dist[s_pos[0]][s_pos[1]] = 0

    while tempq:
        #print(tempq)
        x, y = tempq.popleft() 

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <=nx and nx<n and 0<= ny and ny<n:
                if t_dist[nx][ny] == -1 and graph[nx][ny]<=baby_size:
                    t_dist[nx][ny] = t_dist[x][y]+1
                    tempq.append((nx,ny))
    return t_dist

#가장긴  문자열 lcs

def lcs(word1, word2): 
    max = 0
    index = 0
    letters = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)] 
    for i in range(len(word1)): 
        for j in range(len(word2)): 
            if word1[i] == word2[j]: 
                letters[i+1][j+1] = letters[i][j] + 1 
            if max < letters[i+1][j+1]: 
                max = letters[i+1][j+1]
                index = i + 1 
    return word1[index-max:index] 

#가장 큰 증가하는 수열
n = int(input())
lst = list(map(int, input().split()))

dp = [x for x in lst]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))


#행렬 덧셈
def sumMatrix(A,B):
    answer = []
    for i in range(len(A)): #리스트A,B 구별
        tmp=[] #A출력하고 B 출력하기 위한 구분
        for j in range(len(A[i])): #A와B에 서로 같은 위치의 값 더하기
            tmp.append(A[i][j]+B[i][j]) #Ex) 1+3,2+4
        answer.append(tmp) #첫번째 계산이 끝나면 append
    return answer


#행렬 곱셈

def mulMatrix(A,B):
    answer=[]
    for i in range(0, len(A)):
        temp_row=[]
        for j in range(0, len(B[0])):
            value = 0
            for k in range(0,len(A[0])):
                value += A[i][k]* B[k][j]
            temp_row.append(value)
        answer.append(temp_row)
    return answer



#진법수로 바꾸기
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
#약수
def get_yaksu(num):
    for i in range(1, num+1):
        if num % i == 0:
            # 약수임
            print(i, end=' ')
    print()


#dp 로 가장큰 정사각형 찾으면서 그 리스트들 최대값 찾기(반복문없이)

from itertools import chain
def solution(board):
    height = len(board)
    width = len(board[0])
    for i in range(1, height):
        for j in range(1, width):
            for a in board:
                print(a)
            print()
            mins = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
            if board[i][j] == 0 or mins == 0:
                continue
            board[i][j] = max(mins + 1, board[i][j])
    print(list(chain.from_iterable(board)))
    return max(list(chain.from_iterable(board))) ** 2


#복사를 할떄 리스트안의 리스트 즉 인접행렬 을 복사시에는 copy.deepcopy 를 해야한다.
import copy
def update_board(m,n,board):
    while True:
        temp=copy.deepcopy(board)
        print(temp,1)
        for i in range(m-2,-1,-1):
            for j in range(n-1):
                if board[i][j]!= 0:
                    print(i,j)
                    if board[i+1][j]==0:
                        board[i+1][j]=board[i][j]
                        board[i][j]=0
        print(board,2)
        print(temp,3)
        if board == temp:
            return copy.deepcopy(board)



#하노이 재귀


def hanoi(n, a, b, c,answer):
    if n == 1:
        answer.append([a,c])
        return answer
    else:
        hanoi(n - 1, a, c, b,answer)
        answer.append([a,c])
        hanoi(n - 1, b, a, c,answer)
        
    return answer

