from collections import Counter
import requests
#1
BASE_URL= "https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users"
MAX_CAPACITY = 20
x_auth_token = "f8d1e6f051d46684b3b63a19dfc10e36"
def start():
    uri = BASE_URL + '/start'
    return requests.post(uri, headers={'X-Auth-Token': x_auth_token,"Content-Type": "application/json"}, json={"problem": 1}).json()


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
def get_calls(i):
    uri ="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-"+str(i)+".json"
    return requests.get(uri).json()
def frequent_sort(data):
    #rt_data = set()
    rt_data =Counter(data).most_common()
    return rt_data

jsons=[]
for a in range(1,4):
    jsons.append(get_calls(a))


for n,json in enumerate(jsons):
    borrow_counts1=[]
    back_counts1=[]
    borrow_counts2=[]
    back_counts2=[]
    borrow_counts3=[]
    back_counts3=[]
    for minute in json:
        for temp in json[minute]:
            if int(minute)<=240:
                borrow_counts1.append(temp[0])
                back_counts1.append(temp[1])
            elif int(minute) <=480:
                borrow_counts2.append(temp[0])
                back_counts2.append(temp[1])
            else:
                borrow_counts3.append(temp[0])
                back_counts3.append(temp[1])
    print(n)
    print(frequent_sort(borrow_counts1)[:3])
    print(frequent_sort(
        back_counts1)[:3])
    print()
    print(frequent_sort(borrow_counts2)[:3])
    print(frequent_sort(back_counts2)[:3])
    print()
    print(frequent_sort(borrow_counts3)[:3])
    print(frequent_sort(back_counts3)[:3])
    print()








