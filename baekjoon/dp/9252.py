word1 = input()
word2 = input()


lcs_array=  [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
letter=[["" for i in range(len(word2)+1)] for j in range(len(word1)+1)]

#print(letter)
max_value=0
for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1]:
            lcs_array[i][j] = lcs_array[i-1][j-1]+1
            letter[i][j] += word1[i-1]
        else:
            lcs_array[i][j]= max(lcs_array[i-1][j],lcs_array[i][j-1])             
        if max_value < lcs_array[i][j]:
            max_value = lcs_array[i][j]
#find
word = ""
now = lcs_array[-1][-1]
y= len(lcs_array)-1
x = len(lcs_array[0])-1

while now != 0  :
    if lcs_array[y][x-1] ==now-1 and lcs_array[y-1][x]  ==now-1:
        word = word1[y-1]+ word
        now -=1
        x-=1
        y-=1
    else:
        if lcs_array[y-1][x]> lcs_array[y][x-1]:
            y-=1
        else:
            x-=1

#print(lcs_array[-1][-1])


print(max_value)
if word != "":
    print(word)