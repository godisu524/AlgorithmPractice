
def solution(cards):
    answer = -1
    score = 0
    def card_sum(temp_cards):
        card_score=0
        ones=0
        for a in temp_cards:
            if a >=10:
                card_score+=10
            elif a ==1:
                ones+=1
            else:
                card_score+=a
        while ones != 0:
            if card_score +10 > 21:
                card_score+=1
                ones-=1
            elif 21-(card_score+10) < 21-(card_score+1):
                card_score +=10
            else:
                card_score +=1
        return card_score
    




    def game(cards,score):
        player_card =[]
        diller_card = []
        #print(9)
        player_card.append(cards.pop(0))
        #print(10)
        hidden_card = cards.pop(0)
        diller_card.append(hidden_card)
        player_card.append(cards.pop(0))
        open_card=cards.pop(0)
        diller_card.append(open_card)

        
        if card_sum(player_card)== 21:
            if card_sum(diller_card) != 21:
                score+=3
                return score
            else:
                return score
        elif card_sum(player_card) >21:
            score -=2
            return score
            
        #21미만이라는뜻.
        if open_card in [1,7,8,9,10,11,12,13]:
            #print(1)
            while(card_sum(player_card) <17):
                player_card.append(cards.pop(0))
            if card_sum(player_card) > 21:
                score -=2
                return score
            while(card_sum(diller_card)<17):
                diller_card.append(cards.pop(0))
            if card_sum(diller_card) >21:
                score +=2
                return score

        elif open_card in [4,5,6]:
            #print(2)
            #print(diller_card)
            #print(card_sum(diller_card))
            while card_sum(diller_card)<17:
                diller_card.append(cards.pop(0))
            print(diller_card)
            if card_sum(diller_card) >21:
                score +=2
                
                return score

        elif open_card in [2,3]:
            #print(3)
            while(card_sum(player_card) <12):
                player_card.append(cards.pop(0))
            if card_sum(player_card) > 21:
                score -=2
                return score
            while(card_sum(diller_card)<17):
                diller_card.append(cards.pop(0))
            if card_sum(diller_card) >21:
                score +=2
                return score
        
        if card_sum(player_card) ==21:
            if card_sum(diller_card) !=21:
                score +=3
            else:
                return 0
        if card_sum(player_card) > card_sum(diller_card):
            score +=2
            return score
        elif card_sum(player_card) < card_sum(diller_card):
            score -=2
            return score
        else:
            return score
        
    while(cards):
        #print(cards)
        try:score = game(cards,score)
        except:

            return score




        


    return score



print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))