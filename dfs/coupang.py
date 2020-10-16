
def dfs(graph, v,route,answer):
#    visited[v] = True
    
    print(v, end=" ")
    #print(count)
    route.append(v)
    if v == "YEOSU":
        if "BUSAN" in route:
            answer+=1
            print(route)
        route.clear()
    for i in graph[v]:
        answer=dfs(graph,i,route,answer)
    return answer
    

           
graph = {'ULSAN': ['BUSAN', 'DAEGU'], 
'DAEJEON': ['ULSAN', 'GWANGJU', 'DAEGU'],
 'SEOUL': ['DAEJEON', 'ULSAN'], 
 'GWANGJU': ['BUSAN', 'YEOSU'], 
 'DAEGU': ['GWANGJU', 'BUSAN'], 
 'BUSAN': ['YEOSU'],
 "YEOSU":[]}
#visited = [False]* 9
print(dfs(graph, "SEOUL",[],0))

#{'ULSAN': ['BUSAN', 'DAEGU'], 'DAEJEON': ['ULSAN', 'GWANGJU', 'DAEGU'], 'SEOUL': ['DAEJEON', 'ULSAN'], 'GWANGJU': ['BUSAN', 'YEOSU'], 'DAEGU': ['GWANGJU', 'BUSAN'], 'BUSAN': ['YEOSU']}