class Player:
    def __init__(self,card1,card2, card3= (0,0), card4= (0,0)):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
    def total(self):
        tot = 0
        if self.card1[1]!=0:
            tot+= self.card1[1]
        if self.card2[1]!=0:
            tot+= self.card2[1]
        if self.card3[1]!=0:
            tot+= self.card3[1]
        if self.card4[1]!=0:
            tot+= self.card4[1]
        return tot
    def display(self):
        a=[]
        if self.card1[1]!=0:
            a.append(self.card1)
        if self.card2[1]!=0:
            a.append(self.card2)
        if self.card3[1]!=0:
            a.append(self.card3)
        if self.card4[1]!=0:
            a.append(self.card4)
        return f"Your cards are {a}"