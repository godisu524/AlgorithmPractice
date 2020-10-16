import requests
import random
#1
BASE_URL= "https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users"
MAX_CAPACITY = 20
x_auth_token = "f8d1e6f051d46684b3b63a19dfc10e36"
def start():
    uri = BASE_URL + '/start'
    return requests.post(uri, headers={'X-Auth-Token': x_auth_token,"Content-Type": "application/json"}, json={"problem": 2}).json()


def get_location(auth_key):
    uri = BASE_URL + "/locations"
    return requests.get(uri, headers={'Authorization': auth_key,"Content-Type": "application/json"}).json()

def  get_truck(auth_key):
    uri = BASE_URL + "/trucks"
    return requests.get(uri, headers={'Authorization': auth_key,"Content-Type": "application/json"}).json()

def simulate(auth_key,commands):
    uri = BASE_URL + "/simulate"
    return requests.put(uri, headers={'Authorization': auth_key,"Content-Type": "application/json"},  json={"commands": commands}).json()


def get_score(auth_key):
    uri = BASE_URL + "/score"
    return requests.get(uri, headers={'Authorization': auth_key,"Content-Type": "application/json"}).json()
def get_calls():
    uri ="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-1.json"
    return requests.get(uri).json()

###트럭 함수
def get_truck_empty(trucks,location,bikes_num):
    locationy=location//5
    locationx=location%5
    truck_scores=[]
    for truck in trucks:
        if MAX_CAPACITY- truck["loaded_bikes_count"] >= bikes_num:
            truckx = truck["location_id"]%5
            trucky = truck["location_id"]//5
            truck_scores.append((truck["id"],abs(locationx-truckx)+abs(locationy-trucky)))
    #print(min(truck_scores,key=lambda x:x[1])[0])
    #print(truck_scores)
    if len(truck_scores) == 0:
        return -1
    return min(truck_scores,key=lambda x:x[1])[0]

def get_truck_full(trucks,location,bikes_num):
    locationy=location//5
    locationx=location%5
    truck_scores=[]
    for truck in trucks:
        if  truck["loaded_bikes_count"] >= bikes_num:
            truckx = truck["location_id"]%5
            trucky = truck["location_id"]//5
            truck_scores.append((truck["id"],abs(locationx-truckx)+abs(locationy-trucky)))
    if len(truck_scores) == 0:
        return -1
    return min(truck_scores,key=lambda x:x[1])[0]

def commands_truck(truck_location_id,location_id):
    commands=[]
    #print(truck_location_id,location_id)
    meter = location_id -truck_location_id
    while meter != 0:
        if meter <0:
            if abs(meter) >=5:
                meter +=5
                commands.append(4)
                continue
            else:
                meter +=1
                commands.append(1)
        if meter >0:
            if meter >=5:
                meter -=5
                commands.append(2)
            else:
                meter -=1
                commands.append(3)
    if len(commands) >9:
        return []
    return commands

def commands_random(truck_location_id,size):
    commands=[]
    location_id = (size-1)//2
    #print(truck_location_id,location_id)
    meter = location_id -truck_location_id
    while meter != 0:
        if len(commands) ==10:
            break
        if meter <0:
            if abs(meter) >=5:
                meter +=5
                commands.append(4)
                continue
            else:
                meter +=1
                commands.append(1)
        if meter >0:
            if meter >=5:
                meter -=5
                commands.append(2)
            else:
                meter -=1
                commands.append(3)
    
    return commands

def get_trucks_length(trucks):
    count=0
    for truck in trucks:
        if truck["loaded_bikes_count"] >= 2:
            count+=1
    return count

def get_truck_location(trucks,id):
    for truck in trucks:
        if truck["id"] == id:
            return truck["location_id"]



start_info = start()
auth_key= start_info["auth_key"]

simulations=[]




borrow=[3595,724,969]
back =[3037,2635,2465]
for i in range(720):
    print(i)
    trucks = get_truck(auth_key)
    #trucks = [located_id,loaded_bikes_count]
    locations=get_location(auth_key)
    #location= [id,located_bikes_count]

    trucks = trucks["trucks"]
    locations=locations["locations"]

    done = []
    commands=[]
    t_length = len(trucks)
    #get_trucks_length(trucks)

    for location in locations:
        if location["id"] == back[i//240] :
            continue 
        if t_length ==0:
            break
        if location["located_bikes_count"] <= 2:
            truck_id = get_truck_full(trucks,location["id"],2)
            if truck_id != -1:
                if truck_id not in done:    
                    truck_commands=commands_truck(get_truck_location(trucks,truck_id),location["id"])
                    truck_commands.append(6)
                    truck_commands.append(6)
                    commands.append({ "truck_id": truck_id, "command": truck_commands })
                    done.append(truck_id)
                    t_length-=1
                    continue
    for location in locations:
        if location["id"] == borrow[i//240] :
            continue 
        if location["located_bikes_count"] >=4:
            truck_id = get_truck_empty(trucks,location["id"],1)
            if truck_id != -1:
                if truck_id not in done:
                    truck_commands=commands_truck(get_truck_location(trucks,truck_id),location["id"])
                    truck_commands.append(5)
                    #truck_commands.append(5)
                    commands.append({ "truck_id": truck_id, "command": truck_commands })
                    done.append(truck_id)
                    t_length-=1
                    continue
    for truck in trucks:
        if truck["id"] not in done:
            if truck["loaded_bikes_count"] >= 15:
                truck_commands =commands_random(truck["id"],borrow[i//240])
                commands.append({ "truck_id": truck["id"], "command": truck_commands })
                done.append(truck["id"])
            else:
                truck_commands =commands_random(truck["id"],back[i//240])
                commands.append({ "truck_id": truck["id"], "command": truck_commands })
                done.append(truck["id"])
    
    simulations.append(simulate(auth_key,commands))

    #break






print(simulations)
#print(score_info)
score_info = get_score(auth_key)
print(score_info)




