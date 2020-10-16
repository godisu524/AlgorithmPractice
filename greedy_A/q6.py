food_times = [3,1,2]
k=5

i = 0
while k!=0:
    print(i, food_times)
    if i == len(food_times):
        i = 0
    if food_times[i] != 0:
        food_times[i] -=1 
        k-=1
    else:
        del food_times[i]
        continue
    i+=1
print(i-1)

    
        
            