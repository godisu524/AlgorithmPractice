fibo = [] 
for x in range(5+1): 
    if x <= 2: 
        fibo.append(x)
    else: 
        fibo.append(fibo[x-2] + fibo[x-1]) 
    
print(fibo)

