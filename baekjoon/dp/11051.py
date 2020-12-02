#이항계수 
#n!/k!(n-k)!
from math import factorial
n,k = map(int,input().split())

print((factorial(n)//(factorial(k)*factorial(n-k)))%10007)

