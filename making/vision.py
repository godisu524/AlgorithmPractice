n = int(input())

sec_count=0
min_count=0
hour_count=0
for m in range(n+1):
    if "3" in str(m):
        hour_count+=1
        continue
    for j in range(60):
        for i in range(60):
            if "3" in str(j):
                min_count+=1
                break
            elif "3" in str(i):
                sec_count+=1
print(hour_count*3600+min_count*60+sec_count)


        

    