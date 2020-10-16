def lcs(word1, word2): 
    max = 0
    index = 0
    letters = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)] 
    for i in range(len(word1)): 
        for j in range(len(word2)): 
            if word1[i] == word2[j]: 
                letters[i+1][j+1] = letters[i][j] + 1 
            if max < letters[i+1][j+1]: 
                max = letters[i+1][j+1]
                index = i + 1 
    return word1[index-max:index] 
def solution(m, musicinfos):
    answer = ''
    real_music_info = {}
    real_time_info = {}
    for music in musicinfos:
        start_time= music.split(",")[0]
        end_time= music.split(",")[1]
        music_title=music.split(",")[2]
        music_melody=music.split(",")[3]
        music_melody = music_melody.replace("C#","c")
        music_melody = music_melody.replace("D#","d")
        music_melody = music_melody.replace("F#","f")
        music_melody = music_melody.replace("G#","g")
        music_melody = music_melody.replace("A#","a")


        total_time = (int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1]))-(int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1]))
        print(total_time)
        total_melody = ""
        real_time_info[music_title] = total_time
        count=0
        while total_time != 0:
            total_melody+=music_melody[count]
            count+=1
            if count == len(music_melody):
                count=0
            total_time-=1
        real_music_info[music_title] = total_melody
    #print(real_music_info)


    m = m.replace("C#","c")
    m = m.replace("D#","d")
    m = m.replace("F#","f")
    m = m.replace("G#","g")
    m = m.replace("A#","a")

    for music in real_music_info:
        if m in real_music_info[music]:
            if answer=="":
                answer = music
            else:
                if real_time_info[answer] >= real_time_info[music]:
                    continue
                else:
                    answer=music
    if answer=="":
        answer="(None)"
    return answer


print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))