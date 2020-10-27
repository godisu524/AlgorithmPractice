def solution(s):
    answer = 0

    pc = []

    for i in range(0,len(s)):
        for j in range(1, len(s) +1 ):
            if s[i:j]==s[i:j][::-1]:
                
                pc.append(len(s[i:j]))
            #if s[j:i] and str(s[j:i]) == str(s[j:i])[::-1]:
            #    pc.append(len(s[j:i]))
    print(s[::-1])
    return max(pc)


print(solution("abcbaf"))