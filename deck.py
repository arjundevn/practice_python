import random

def create_deck():
    '''
    creates deck
    '''
    type = ['Spades', 'Clubs', 'Hearts','Diamonds']
    deck = []
    
    for i in type:
        for j in range (1,14):
            if j ==1:
                deck.append((i,'Ace'))
            elif j ==11:
                deck.append((i,'Jack'))
            elif j ==12:
                deck.append((i,'Queen'))
            elif j ==13:
                deck.append((i,'King'))
            else:
                deck.append((i,j))
    return deck


def shuffle_deck(deck):
    '''
    shuffles deck
    '''
    random.shuffle(deck)

    
d = create_deck()
shuffle_deck(d)
print(d)