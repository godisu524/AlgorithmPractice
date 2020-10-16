def solution(roads):
    #graph.sort(reverse=True)
    

    routes={}
    for t1, t2 in roads:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    st = ['ULSAN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    
    return ans
graph = {'ULSAN': ['BUSAN', 'DAEGU'], 'DAEJEON': ['ULSAN', 'GWANGJU', 'DAEGU'], 'SEOUL': ['DAEJEON', 'ULSAN'], 'GWANGJU': ['BUSAN', 'YEOSU'], 'DAEGU': ['GWANGJU', 'BUSAN'], 'BUSAN': ['YEOSU']}
#visited = [False]* 9
print(solution([["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
    
