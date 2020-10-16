import math
MAX_CAPACITY = 20
#array=[[4,9,14,19,24]

trucks = [{'id': 0, 'loaded_bikes_count': 4, 'location_id': 2},
{'id': 1, 'loaded_bikes_count': 17, 'location_id': 10},
{'id': 2, 'loaded_bikes_count': 10, 'location_id': 7},
{'id': 3, 'loaded_bikes_count': 4, 'location_id': 24},
{'id': 4, 'loaded_bikes_count': 5, 'location_id': 5}]
    
locations=[
    {'id': 0, 'located_bikes_count': 4},
{'id': 1, 'located_bikes_count': 1},
{'id': 2, 'located_bikes_count': 4},
{'id': 3, 'located_bikes_count': 4},
{'id': 4, 'located_bikes_count': 4},
{'id': 5, 'located_bikes_count': 8},
{'id': 6, 'located_bikes_count': 4},
{'id': 7, 'located_bikes_count': 4},
{'id': 8, 'located_bikes_count': 4},
{'id': 9, 'located_bikes_count': 4},
{'id': 10, 'located_bikes_count': 4},
{'id': 11, 'located_bikes_count': 9},
{'id': 12, 'located_bikes_count': 4},
{'id': 13, 'located_bikes_count': 4},
{'id': 14, 'located_bikes_count': 4},
{'id': 15, 'located_bikes_count': 4},
{'id': 16, 'located_bikes_count': 3},
{'id': 17, 'located_bikes_count': 4},
{'id': 18, 'located_bikes_count': 4},
{'id': 19, 'located_bikes_count': 4},
{'id': 20, 'located_bikes_count': 2},
{'id': 21, 'located_bikes_count': 4},
{'id': 22, 'located_bikes_count': 4},
{'id': 23, 'located_bikes_count': 4},
{'id': 24, 'located_bikes_count': 4}
]

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
    if len(commands) >6:
        return []
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
done = []
commands=[]
t_length = len(trucks)
#get_trucks_length(trucks)

for location in locations:
    if t_length ==0:
        break
    if location["located_bikes_count"] <= 2:
        truck_id = get_truck_full(trucks,location["id"],2)
        if truck_id not in done:
            truck_commands=commands_truck(get_truck_location(trucks,truck_id),location["id"])
            truck_commands.append(6)
            truck_commands.append(6)
            commands.append({ "truck_id": truck_id, "command": truck_commands })
            done.append(truck_id)
            t_length-=1
            continue
for location in locations:
    if location["located_bikes_count"] >=6:
        truck_id = get_truck_empty(trucks,location["id"],2)
        if truck_id not in done:
            truck_commands=commands_truck(get_truck_location(trucks,truck_id),location["id"])
            truck_commands.append(5)
            truck_commands.append(5)
            commands.append({ "truck_id": truck_id, "command": truck_commands })
            done.append(truck_id)
            t_length-=1
            continue
        
print(done)
print(commands)



            




    



    

get_truck_empty(trucks,11,2)
    