import deck
from player_class import Player

d = deck.create_deck()
#d= [('Spades', 10), ('Diamonds', 'King'), ('Hearts', 'Ace'), ('Spades', 'Ace'), ('Diamonds', 7), ('Diamonds', 4)]
deck.shuffle_deck(d)
print(d)
def check_total(a,b):
    if a > 21 and b is True:
        print("You Lost")
        exit()
    if a > 21 and b is False:
        print("You Won!!")
        exit()
       
h = [d.pop(),d.pop()]
c = [d.pop()]

def update_hand(h,c):
	hm = Player(h)
	com = Player(c)
	print("Your")
	hm.display()
	m = hm.total()
	print(f"Your total is {m}")
	check_total(m, True)
	print("Computer's")
	com.display()
	t= 0
	for x in range(0,len(c)):
		if c[x][1] =='Ace':
			if (t+11)<= 21:
				t+=11
			else:
				t+=1
		elif c[x][1] =='King' or c[x][1] == 'Queen' or c[x][1] == 'Jack':
			t+=10
		else:
			t+=c[x][1]
	print(f"Computer's total is {t}")
	check_total(t, False)
	print("---------------------------")
	return (m,t)

def check_result(m):
	if abs(21-m[0])<abs(21-m[1]):
		print ("You Won ")
	elif abs(21-m[0])==abs(21-m[1]):
		print ("Draw")
	else:
		print ("You Lost")


def ip():
	u = str(input("Do you want to  HIT or STAY?"))
	print(u)
	if u.lower() == 'hit':
		h.append(d.pop())
		update_hand(h,c)
		ip()
	if u.lower() == 'stay':
		c.append(d.pop())
		f= update_hand(h,c)
		check_result(f)

update_hand(h,c)
ip()







