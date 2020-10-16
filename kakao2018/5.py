def solution(msg):
    answer = []
    total_dict = {}
    for n,i in enumerate(range(ord("A"),ord("Z")+1)):
        total_dict[chr(i)]=n+1


    temp=""
    for n,letter in enumerate(msg):
        temp+=letter
        
        #if n == len(msg) and len(temp)==1:
        #    answer.append(total_dict[temp])
            

        if temp in total_dict:
            continue
        else:
            total_dict[temp] = len(total_dict)+1
            answer.append(total_dict[temp[:-1]])
            temp=temp[-1]
    answer.append(total_dict[temp])
    

   # print(answer)



    return answer



print(solution("ABABABABABABABAB"))