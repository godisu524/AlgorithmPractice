alphabet=  "abcdefghijklmnopqrstuvwxyz"
def solution(encrypted_text, key, rotation):
    encrypted_text=list(encrypted_text)
    
    if rotation < 0:
        rotation = -rotation
        for i in range(rotation):
            temp = encrypted_text.pop()
            encrypted_text.insert(0,temp)
    else:
        for i in range(rotation):
            temp = encrypted_text.pop(0)
            encrypted_text.append(temp)
    

    for i in range(len(encrypted_text)):
        temp = ord(encrypted_text[i])-(alphabet.index(key[i])+1)
        if ord("a") <= temp <= ord("z"):
            encrypted_text[i]=chr(temp)
        else:
            encrypted_text[i]=chr(temp+26)
    #print(encrypted_text)
    
    return "".join(encrypted_text)
    
    


print(solution("qyyigoptvfb", "abcdefghijk", 3))