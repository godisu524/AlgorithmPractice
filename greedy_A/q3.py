n = input()

zeros = n.count("0")
if zeros >= len(n):
    default_num = "0"    
else:
    default_num = "1"

mystr=n[0]
for i in range(1,len(n)):
    if n[i] != mystr[-1]:
        mystr+=n[i]



print(mystr.count(default_num))

