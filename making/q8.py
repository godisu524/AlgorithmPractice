import re
n=input()
m=n

m=re.compile('[0-9]+').sub('', m)
n=re.compile('[^0-9]+').sub('', n)

m=list(m)
n=list(n)
m.sort()
n.sort()

m="".join(m)
n="+".join(n)
print(m+str(eval(n)))

