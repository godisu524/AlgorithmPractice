n = int(input())
dp=[1]
count = 2
while True:
    if len(dp) == n:
        break
    else:
        i = count
        while True :
            print(i)
            print(dp)
            if i in dp:
                if count not in dp:
                    dp.append(count)
                    count+=1
                    break
                else:
                    count+=1
                    break
            if i % 2 == 0:
                i //= 2    
                continue
            if i % 3 == 0:
                i//=3
                continue
            if i % 5 == 0:
                i//=5
                continue
            count +=1
            break


print(dp[-1])