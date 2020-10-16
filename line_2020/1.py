def solution(boxes):
    answer = 0
    box_count=0
    box_data= [0 for _ in range(len(boxes*2)+1)]

    for box in boxes:
        if box[0] == box[1]:
            box_count+=1
            continue
        else:
            box_data[box[0]]+=1
            box_data[box[1]]+=1
    print(box_data)

    for i in box_data:
        if i != 0:
            if i % 2 == 0:
                box_count+=1
                continue
    

                
    

    return len(boxes) - box_count



print(solution([[1, 2], [3, 4], [5, 6]]))