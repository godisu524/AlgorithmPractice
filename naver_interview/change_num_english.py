num_dict={}
num_dict["0"]=""
num_dict["00"]=""
num_dict["1"] = "one"
num_dict["2"] = "two"
num_dict["3"] = "three"
num_dict["4"] = "four"
num_dict["5"] = "five"
num_dict["6"] = "six"
num_dict["7"] = "seven"
num_dict["8"] = "eight"
num_dict["9"] = "nine"
num_dict["10"] = "ten"
num_dict["11"] = "eleven"
num_dict["12"] = "twelve"
num_dict["13"] = "thirteen"
num_dict["14"] = "fourteen"
num_dict["15"] = "fifteen"
num_dict["16"] = "sixteen"
num_dict["17"] = "seventeen"
num_dict["18"] = "eighteen"
num_dict["19"] = "nineteen"
num_dict["20"] = "twenty"
num_dict["30"] = "thirty"
num_dict["40"] = "fourty"
num_dict["50"] = "fifty"
num_dict["60"] = "sixty"
num_dict["70"] = "seventy"
num_dict["80"] = "eighty"
num_dict["90"] = "ninety"
num_dict["100"] = "one hundred"



cost = ["million", "thousand",""]
cost.reverse()
#...

num = 2111000
numlist = list(str(num))
count = 3
temp=[]
index=0
ans=""
while numlist:
    tempstr=""
    temp.insert(0,numlist.pop())
    count-=1
    print(temp)
    if count == 0:
        count = 3 
        tempstr+=num_dict[str(temp.pop(0))] +" "+ "hundred"
        tens=str(temp.pop(0))
        if tens == "1":        
            tempstr+=" "+num_dict[tens+str(temp.pop(0))] + " " + cost[index] +" "
        else:
            tempstr+=" "+num_dict[str(tens)+"0"]
            tempstr+=" "+num_dict[str(temp.pop(0))]+" "+ cost[index]+" "
        index+=1
        ans = tempstr +ans 
if len(temp) == 2:
    tens=str(temp.pop(0))
    if tens == "1":        
        tempstr+=" "+num_dict[tens+str(temp.pop(0))] + " " + cost[index] +" "
    else:
        tempstr+=" "+num_dict[str(temp.pop(0))+"0"]
        tempstr+=" "+num_dict[str(temp.pop(0))]+" "+ cost[index]+" "
    ans = tempstr +ans 
else:
    tempstr+=" "+num_dict[str(temp.pop(0))]+" "+ cost[index]+" "
    ans = tempstr +ans 

        
    
print(temp)
print(ans.strip())



