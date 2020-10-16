import re
from itertools import groupby
def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = re.compile('[^0-9a-z-_.]+').sub('', new_id)
    #3
    temp_str = ""
    count=0
    for char in new_id:
        if char != ".":
            temp_str+= char
            count=0
        else:
            if count == 0:
                temp_str+=char
                count+=1
            else:
                continue
    new_id= temp_str

    #4
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:-1]
    print(new_id)

    #5
    if len(new_id) == 0:
        new_id = "a"
    
    #6
    print(len(new_id))
    if len(new_id)>=16:
        new_id = new_id[:15]
    print(len(new_id))
    if new_id.endswith("."):
        new_id = new_id[:-1]

    #7
    if len(new_id)<=2 :
        while len(new_id)!=3:
            new_id+=new_id[-1]
    
    

    return new_id




print(solution("...!@BaT#*..y.abc55defghijklm.."))