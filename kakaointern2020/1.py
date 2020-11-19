from itertools import permutations


def diverseDeputation(m, w):
    # Write your code here
    ans=0
    if m == 0 or w == 0 or (m+w)<3:
        return 0
    #무조건 세명을뽑음
    #남자 두명 여자 한명의 경우
    if m>=2:
        ans+=((m*(m-1))/2)*w
    if w>=2:
        ans+=((w*(w-1))/2)*m
    
    return int(ans)

    

print(diverseDeputation(3,9))