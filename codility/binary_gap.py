# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(N):
    # write your code in Python 3.6
    n= convert(N,2)
    start_flag= False
    finish_flag = False
    max_count=0
    count=0
    #print(n)

    for i in list(n):
        
        if i == "1":
            #print(i)
            if start_flag:
                #print(1)
                max_count=max(max_count,count)
                count=0
            else:
                #print(2)
                start_flag=True
        else:
            #print(3)
            if start_flag:
                count+=1

    return max_count

print(solution(1041))