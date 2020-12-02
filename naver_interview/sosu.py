import math
def check(n):
    k = math.sqrt(n)

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

num = int(input())

for i in range(2,num+1):
    if check(i):
        print(i)