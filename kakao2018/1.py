def check_length(number,hand):
    number_array=[[1,2,3],[4,5,6],[7,8,9],[-1,0,99]]
    for i in range(len(number_array)):
        for j in range(len(number_array[0])):
            if number_array[i][j]==number:
                a_x=i
                a_y=j
                continue
            if number_array[i][j]==hand:
                b_x=i
                b_y=j
                continue
    return abs(a_x-b_x)+abs(a_y-b_y)
def solution(numbers, hand):
    left_hand=-1
    right_hand=99
    answer = ''
    for num in numbers:
        if num in [1,4,7]:
            answer+= "L"
            left_hand=num
        elif num in [3,6,9]:
            answer+="R"
            right_hand=num
        else:
            if check_length(num,left_hand) > check_length(num,right_hand) :
                answer+="R"
                right_hand=num
            elif check_length(num,left_hand) < check_length(num,right_hand):
                answer+="L"
                left_hand = num
            else:
                if hand == "right":
                    answer+="R"
                    right_hand=num
                else:
                    answer+="L"
                    left_hand= num

        

    return answer

print(solution([5,2,8,0,1,5,2,4, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5,0,7,6,5,4,2,1,7,8,7,4,5],"right"))



