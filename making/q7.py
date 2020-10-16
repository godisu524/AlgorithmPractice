n= input()

if eval("+".join(n[:len(n)//2])) == eval("+".join(n[(len(n)//2):])):
    print("LUCKY")
else:
    print("READY")



