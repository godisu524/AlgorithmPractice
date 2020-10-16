def solution(s, n):
    answer = ''
    s=list(s)
    print(s)
    #print(s)
    for i in range(len(s)):
        if s[i] != " ":
            if ord(s[i]) in range(ord("a"),ord("z")+1):
                if ord(s[i])+n > ord("z"):
                    s[i]= chr(ord(s[i])+n-26)
                else:
                    s[i] = chr(ord(s[i])+n)
            if ord(s[i]) in range(ord("A"),ord("Z")+1):
                if ord(s[i])+n > ord("Z"):
                    s[i]= chr(ord(s[i])+n-26)
                else:
                    s[i] = chr(ord(s[i])+n)


        
    answer = "".join(s)
    return answer


print(solution(	"a B z", 4))
