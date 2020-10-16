string = input()

max_len = len(string)
results=[]
count=1
pre=""
for i in range(1,max_len//2+1):
    pre=""
    end=""
    for j in range(0,max_len,i):
        temp=string[j:j+i]
        print(temp)
        if j == 0:
            pre = temp
            continue
        if pre == temp:
            count+=1        
            continue
        else:
            if count ==1:
                end+= pre
                pre = temp
            else:
                end+= str(count) +pre
                pre = temp
                count=1
    if count ==1:
            end+= pre
    else:
        end+= str(count) +pre
        count=1
        
    #results.append(len(end))
    results.append(len(end))
print(min(results))
#print(max(results))
        #if string[j:j+2] not in word_dic:
        #    word_dic[string[j:j+2]] = 1
        #else:
        #    word_dic[string[j:j+2]] += 1
    
    
