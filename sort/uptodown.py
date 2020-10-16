n = int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
#reversed 아니고 reverse
numbers.sort(reverse=True)


print(numbers)