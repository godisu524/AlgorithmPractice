#MultiSet
def solution(str1, str2):
    array1=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            array1.append(str1[i].lower()+str1[i+1].lower())
    array2=[]
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            array2.append(str2[i].lower()+str2[i+1].lower())


    if len(array1) == 0 and len(array2) == 0:
        return 65536
    total_array=[]
    hap= 0
    for a in array1:
        if a not in total_array:
        
            for _ in range(max(array1.count(a),array2.count(a))):
                total_array.append(a)
                    
                
                    #print(hap,a)
            hap += min(array1.count(a),array2.count(a))
    #A엔 없는데 B에 여러개일 수 있음.
    for b in array2:
        if b not in total_array:
            for _ in range(max(array1.count(b),array2.count(b))):
                total_array.append(b)
    print(sorted(array1))
    print(sorted(array2))
    print(total_array)
    print(hap,len(total_array))
    return int((hap/len(total_array))*65536)
    
    
    


    



    

print(solution("CCDEFGHH","ABCCC"))