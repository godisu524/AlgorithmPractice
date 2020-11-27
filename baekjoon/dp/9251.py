word1 = input()
word2 = input()


lcs_array=  [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
max_value=0
for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1]:
            lcs_array[i][j] = lcs_array[i-1][j-1]+1
        else:
            lcs_array[i][j]= max(lcs_array[i-1][j],lcs_array[i][j-1])
        if max_value < lcs_array[i][j]:
            max_value = lcs_array[i][j]

#print(lcs_array[-1][-1])


print(max_value)