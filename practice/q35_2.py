n = int(input())

ugly=[0] * n
ugly[0]=1


i2=i3=i5= 0
next2,next3,next5 = 2,3,5
#결론은 1*2,3,5 값인데 이제 작은순서대로 나열해야하니까 인덱스로해서 계싼 ㅇㅋ 좋네 
#내방식도 나쁘진않앗어 근데 dp 개념에서는 이친구꺼가 맞는듯.
for i in range(1,n):
    ugly[i] = min(next2,next3,next5)
    
    if ugly[i] == next2:
        i2+=1
        next2 = ugly[i2] * 2
    
    if ugly[i] == next3:
        i3+=1
        next3 = ugly[i3] * 3
    

    if ugly[i] == next5:
        i5+=1
        next5 = ugly[i5] * 5

print(ugly[n-1])