n, m = map(int,input().split())

numbers = list(map(int,input().split()))

array = [0]* 11

for x in numbers:
    array[x]+=1


result = 0
#뽑은갯수 * 나머지 뽑을수있는것 갯수
#총갯수에서 뽑은갯수 계속 - 로 갱신
for i in range(1, m +1):
    n -= array[i]
    result += array[i]* n

print(result)