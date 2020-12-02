n = int(input())
index=0
size = ["KiB", "MiB", "GiB", "TiB","PiB","EiB","ZiB","YiB"]
while True:
    if n <= 1024:
        print(str(round(n,1)) + " " + size[index])
        break
    else:
        n/=1024
        index+=1

