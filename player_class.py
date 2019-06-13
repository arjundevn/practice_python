class Player:
    def __init__(self,hand,tot = 0):
        self.hand = hand
        self.tot = tot
    def display(self):
        print("Your cards are:")
        for x in range(0,len(self.hand)):
            print(f"{self.hand[x][1]} of {self.hand[x][0]}")
    def total(self):
        for x in range(0,len(self.hand)):
            try:
                self.tot+= self.hand[x][1]
            except:
                if self.hand[x][1] == 'King' or self.hand[x][1] == 'Queen' or self.hand[x][1] == 'Jack':
                    self.tot+= 10
                elif self.hand[x][1] == 'Ace':
                    while True:
                        ace = int(input('Please select 1 or 11 for Ace:'))
                        if ace ==1:
                            self.tot+= 1
                            break
                        elif ace ==11:
                            self.tot+= 11
                            break
        return f"TOTAL IS {self.tot}"