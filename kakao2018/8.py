def solution(cacheSize, cities):
    answer = 0
    cache=[0 for _ in range(cacheSize)]
    if cacheSize==0:
        return 5*len(cities)

    print(cache)
    for city in cities:
        city= city.lower()
        if city in cache:
            cache.pop(cache.index(city))
            cache.append(city)
            answer+=1
        else:
            cache.pop(0)
            cache.append(city)
            answer+=5
    return answer




print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))