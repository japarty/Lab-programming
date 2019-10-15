import random

def deck_generator():
    deck = []
    for i in range(2,14):
        for j in ['♥','♦','♣','♠']:
            deck.append([i,j])
    return deck

def proper_name(card):
    if card[0] == 11:
        return("J"+str(card[1]))
    elif card[0] == 12:
        return("Q"+str(card[1]))
    elif card[0] == 13:
        return("K"+str(card[1]))
    elif card[0] == 14:
        return("A",card[1])
    else:
        return(str(card[0])+str(card[1]))

def deal_cards(deck):
    deck_p_1 = []
    deck_p_2 = []
    while len(deck)>0:
        deck_p_1.append(deck[0])
        deck.remove(deck[0])
        deck_p_2.append(deck[0])
        deck.remove(deck[0])
    return deck_p_1,deck_p_2

deck = deck_generator()
random.shuffle(deck)
deck_p_1,deck_p_2 = deal_cards(deck)

def war(deck_p_1,deck_p_2):
    i = 0
    while len(deck_p_1)>0 and len(deck_p_2)>0:
        i += 1
        curr_card_p_1 = deck_p_1.pop(0)
        curr_card_p_2 = deck_p_2.pop(0)
        print(len(deck_p_1),len(deck_p_2),len(deck_p_1)+len(deck_p_2))
        print(proper_name(curr_card_p_1),"vs",proper_name(curr_card_p_2)) #sprawdzanie
        if curr_card_p_1[0]>curr_card_p_2[0]:
            deck_p_1.append(curr_card_p_1)
            deck_p_1.append(curr_card_p_2)
            print("PLAYER ONE WON THE ROUND")
        elif curr_card_p_2[0]>curr_card_p_1[0]:
            deck_p_2.append(curr_card_p_2)
            deck_p_2.append(curr_card_p_1)
            print("PLAYER TWO WON THE ROUND")
        elif curr_card_p_1[0] == curr_card_p_2[0]:
            stake = []
            if_stop = 0
            while if_stop == 0:
                if len(deck_p_1)>1 and len(deck_p_2)>1:
                    print("WAR")
                    stake.extend([curr_card_p_1,curr_card_p_2,deck_p_1.pop(0),deck_p_2.pop(0)])
                    curr_card_p_1 = deck_p_1.pop(0)
                    curr_card_p_2 = deck_p_2.pop(0)
                    print(len(deck_p_1),len(deck_p_2),len(deck_p_1)+len(deck_p_2))
                    print(curr_card_p_1[0],curr_card_p_2[0]) #sprawdzanie
                    if curr_card_p_1[0]>curr_card_p_2[0]:
                        deck_p_1.extend(stake)
                        deck_p_1.append(curr_card_p_1)
                        deck_p_1.append(curr_card_p_2)
                        if_stop = 1
                    elif curr_card_p_2[0]>curr_card_p_1[0]:
                        deck_p_2.extend(stake)
                        deck_p_2.append(curr_card_p_2)
                        deck_p_2.append(curr_card_p_1)
                        if_stop = 1
                elif len(deck_p_1)<2:
                    print("PLAYER TWO WON THE GAME ")
                    break
                elif len(deck_p_2)<2:
                    print("PLAYER ONE WON THE GAME")
                    break
    if len(deck_p_1) == 0:
        print("PLAYER TWO WON THE GAME")
    elif len(deck_p_2) == 0:
        print("PLAYER ONE WON THE GAME ")
    print(i)

war(deck_p_1,deck_p_2)
