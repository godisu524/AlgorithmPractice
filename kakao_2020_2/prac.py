import requests
import json

url = 'http://2019-kakao-practice.encrypted.gg:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def simulator():
    user = 'tester'
    problem = 0
    count = 4
    elv = [
        {
            "elevator_id":0,
            "command":"STOP",
            "call_ids":[]
        },
        {
            "elevator_id": 1,
            "command": "STOP",
            "call_ids": []
        },
        {
            "elevator_id": 2,
            "command": "STOP",
            "call_ids": []
        },
        {
            "elevator_id": 3,
            "command": "STOP",
            "call_ids": []
        },
    ]
    maxx=[5,25,25]
    curr = [1,1,1,1]  #현재층
    human = [0,0,0,0]   #담긴 인간
    state = [0,0,0,0] #0STOPED 1OPENED 2UPWARD 3DOWNWARD
    check = [0,0,0,0]
    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    while(1):
        flag =[0,0,0,0]
        temp = oncalls(token)
        jstr=json.dumps(temp)
        str=json.loads(jstr)
        #print(str)
        if(str["is_end"]):
            break

        
        for elevator in str["elevators"]:
            for passenger in elevator["passengers"]:
                if(curr[elevator["id"]]==passenger["end"]):
                    if(state[elevator["id"]]==0 and flag[elevator["id"]]==0):
                        elv[elevator["id"]]["command"]="OPEN"
                        state[elevator["id"]]=1
                        flag[elevator["id"]]=1
                    elif(state[elevator["id"]] == 1 and (flag[elevator["id"]]==0 or flag[elevator["id"]]==2)):
                        elv[elevator["id"]]["command"] = "EXIT"
                        state[elevator["id"]] = 1
                        flag[elevator["id"]] = 2
                        elv[elevator["id"]]["call_ids"].append(passenger["id"])
                        human[elevator["id"]] -= 1
                    elif(state[elevator["id"]] == 2 and flag[elevator["id"]]==0):
                        elv[elevator["id"]]["command"] = "STOP"
                        state[elevator["id"]] = 0
                        flag[elevator["id"]] = 1
                    elif(state[elevator["id"]] == 3 and flag[elevator["id"]]==0):
                        elv[elevator["id"]]["command"] = "STOP"
                        state[elevator["id"]] = 0
                        flag[elevator["id"]] = 1

        for call in str["calls"]:
            for i in range(4):
                if(human[i]==8):
                    continue
                if(flag[i]==0 and curr[i]==call["start"]):
                    if(state[i]==0):
                        elv[i]["command"]="OPEN"
                        state[i]=1
                        flag[i] = 1
                        break
                    elif(state[i]==1 and human[i]<8):
                        elv[i]["command"] = "ENTER"
                        state[i] = 1
                        elv[i]["call_ids"].append(call["id"])
                        human[i] += 1
                        flag[i] = 1
                        break
                    elif(state[i]==2):
                        elv[i]["command"] = "STOP"
                        state[i] = 0
                        flag[i] = 1
                        break
                    elif(state[i]==3):
                        elv[i]["command"] = "STOP"
                        state[i] = 0
                        flag[i] = 1
                        break

        for i in range(4):
            if(flag[i]==0):
                if(state[i]==0):
                    if (curr[i] == maxx[problem]):
                        elv[i]["command"] = "DOWN"
                        curr[i] -= 1
                        check[i] = 1
                        state[i] = 3
                        continue
                    elif (curr[i] == 1):
                        elv[i]["command"] = "UP"
                        curr[i] += 1
                        check[i] = 0
                        state[i] = 2
                        continue
                    if(check[i]==0):
                        elv[i]["command"]="UP"
                        state[i]=2
                        curr[i]+=1
                    else:
                        elv[i]["command"]="DOWN"
                        state[i]=3
                        curr[i]-=1
                elif(state[i]==1):
                    elv[i]["command"]="CLOSE"
                    state[i]=0
                elif(state[i]==2):
                    if(curr[i]==maxx[problem]):
                        elv[i]["command"]="STOP"
                        state[i]=0
                        check[i]=1
                    else:
                        elv[i]["command"]="UP"
                        state[i]=2
                        curr[i]+=1
                elif(state[i]==3):
                    if(curr[i]==1):
                        elv[i]["command"]="STOP"
                        state[i]=0
                        check[i]=0
                    else:
                        elv[i]["command"]="DOWN"
                        state[i]=3
                        curr[i]-=1
        print(curr)
        print(human)
        print(state)
        print(check)
        temp2=action(token,[elv[0],elv[1],elv[2],elv[3]])
        print(temp2)
        for i in range(count):
            elv[i]['call_ids']=[]

if __name__ == '__main__':
    simulator()


