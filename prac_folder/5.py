def lcs(word1, word2): 
    max = 0
    index = 0
    letters = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)] 
    #print(letters)
    for i in range(len(word1)): 
        for j in range(len(word2)): 
            if word1[i] == word2[j]: 
                letters[i+1][j+1] = letters[i][j] + 1 
            if max < letters[i+1][j+1]: 
                max = letters[i+1][j+1]
                index = i + 1 
    return len(word1[index-max:index])

word1 = input()
word2= input()

print(lcs(word1,word2))


