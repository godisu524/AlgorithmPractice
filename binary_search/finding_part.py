import sys
n= int(input())
N = list(map(int,sys.stdin.readline().rstrip().split()))
N.sort()
m = int(input())
M= list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start+end) //2

    if array[mid] == target:
        return True
    elif array[mid] >target :
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
for i in M:
    if binary_search(N,i,0,n-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")