def editDistance(source, target):
    alphabet=  "abcdefghijklmnopqrstuvwxyz"
    ans = 0

    def shift(source,index):
        t_source=list(source)
        for i in range(len(t_source)):
            temp = ord(t_source[i])+index
            if ord("a") <= temp <= ord("z"):
                t_source[i]=chr(temp)
            else:
                t_source[i]=chr(temp-26)
        #print(t_source)
        return t_source


    
    def check(source,target):
        t_target=list(target)
        s_source =list(source)
        s_index=0
        
        max_count=0
        for td in range(len(target)):
            count=0    
            s_index=0
            s_source =list(source[td:])
            for t in t_target:
                if t in s_source[s_index:]:
                    s_index = s_source[s_index:].index(t)+s_index
                    count+=1
            max_count=max(max_count,count)
        return max_count


    shifted_source=[]
    
    for i in range(len(alphabet)+1):
        shifted_source.append(shift(source,i))
    
    max_count=0
    for ss in shifted_source:
        max_count = max(check(ss,target),max_count)

    return (len(target) - max_count)*2
    

    # print(check(shifted_source[0],target))
    #for ss in shifted_source:
        

        

  








print(editDistance("mqfsnmygrquczhymvkurxfelpeagkisearktnjrcapbuuawnmcrgsfsnusuprtnnzbuvtoemgiohvicsnkqhbgoomupuvjmfzpqp","yelitmysnjcfgvvvezaprgaonzkofyqqhfmxseezencanocepyzxocwivnkbjrhcehqlcwsagrfookhiwsrjguzonapppyyodlqx"))


