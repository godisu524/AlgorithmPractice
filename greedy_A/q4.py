def coin():
    n = int(input())
    coins = list(map(int,input().split()))

    coins.sort()
    #1이 있는것을 확인한다.
    target = 1
    
    for coin in coins:
        if target < coin:
            break
        target += coin

        
    print(target)        
        


coin()