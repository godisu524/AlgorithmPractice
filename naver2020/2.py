def count_childs(edge,array,count=0):
        for e in array[edge]:
            if e != -1:
                count+=1
                count+= count_childs(e,array)
        return count
def solution(n,edges):
    array=[[-1] for i in range(n)]    
    for edge in edges:
        array[edge[0]].append(edge[1])
    start=0
    min_value=1
    
    q=[start]
    
    while True:
        temp_array=[]
        min_value=999
        
        for e in q:
            if len(array[e]) <min_value :
                temp_array.clear()
                temp_array.append(e)
                min_value=len(array[e])
            elif len(array[e])==min_value:
                temp_array.append(e)
        if len(temp_array) != 1:
            t_max = 0
            for t in temp_array:
                if count_childs(t) >=t_max:
                    cut = t
                    t_max = count_childs(t)
        else:
            cut = temp_array[0]
        print(cut)
        for a in array:
            try:
                a.remove(cut)
            except:
                None
        while len(q):
            temp=q.pop(0)
            for a in array[temp][1:]:
                q.append(a)
        print(array)
        
        return count_childs(0)
        
        

                
            
        
    
    
    



print(solution(19,[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))