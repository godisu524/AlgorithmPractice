# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    ans=0
    nums={}
    max_num = max(A)
    for i in A:
        try:
            nums[i] +=1
        except:
            nums[i] = 1
    
    for num in nums:
        if nums[num] ==2:
            ans+=2
        else:
            ans+=1
    if nums[max_num] ==2:
        ans-=1
    return ans

    
    



    
    
    
    




print(solution([2,5,3,2,4,1]))