def solution(record):
    answer = []

    temp_order=[]
    users={}
    for r in record:
        order = r.split()[0]
        uid = r.split()[1]
        if order != "Leave":
            nickname=r.split()[2]

        if order == "Enter":
            users[uid]=nickname
        
        elif order == "Change":
            users[uid]=nickname

    for r in record:
        order = r.split()[0]
        uid = r.split()[1]

        if order == "Enter":
            temp_order.append(users[uid]+"님이 들어왔습니다.")    
        elif order == "Leave":
            temp_order.append(users[uid]+"님이 나갔습니다.")    
            
        





    return temp_order



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))