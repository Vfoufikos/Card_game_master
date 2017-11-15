from playing_cards import *



def computer_plays():
	global d, table, computer_hand, what_happened

	target_val=table[-1].value
	target_sym=table[-1].symbol
	
	while(True):
		for c in computer_hand: 
			if c.value==target_val or c.symbol==target_sym:
				print("PC drops ",c)
				computer_hand.remove(c)
				table.append(c)
				what_happened="computer_played"
				return
		new_card=d.draw()
		if new_card=="empty":
			what_happened="deck finished"
			return 
		else:
			print("PC takes a new card")
			computer_hand.append(new_card)

def print_info():
	global d, table, computer_hand, human_hand
	print()
	print("Deck has ", len(d.content), " cards")
	print("PC has ", len(computer_hand), "cards")
	print("On table are ", len(table), "cards")
	print("The card on the top is ", table[-1])
	print("Your cards are ", len(human_hand))
	HHS=[str(x) for x in human_hand]
	print(HHS)
	print()
	print("Choose card to drop or press enter to pull a new card")

def human_plays():
	global d, table, human_hand, what_happened
	while True:
		print_info()
		sel=input()
		if sel=="":
			new_card=d.draw()
			if new_card=="empty":
				what_happened="deck finished"
				return
			else:
				human_hand.append(new_card)
		else:
			HHS=[str(x) for x in human_hand]
			if not (sel in HHS):
				print(sel, "??? Dont have this card")
			else:
				t=table[-1]
				target_val=t.value
				target_sym=t.symbol
				if sel[0]!=target_val and sel[1]!=target_sym:
					print("You cant drop this card", sel)
				else:
					print("You drop ", sel)
					ind=HHS.index(sel)
					selc=human_hand[ind]
					human_hand.remove(selc)
					table.append(selc)
					what_happened="human_played"
					return

def initial():
	global d, table, computer_hand, human_hand, what_happened
	print("Take the cards")
	d.collect()
	table=[]
	computer_hand=[]
	human_hand=[]
	print("Shuffle the deck")
	d.shuffle()
	print("Give cards to players")
	table.append(d.draw())
	print("The card in table is ", table[-1])
	for i in range(7):
		human_hand.append(d.draw())
		computer_hand.append(d.draw())
	print("Flip the coin", end=" ")
	if random.random()<0.5:
		print("You play first")
		what_happened="computer_played"
	else:
		print("... PC play first")
		what_happened="human_played"


def evaluate():
	global computer_hand, human_hand, what_happened
	if what_happened==human_wins:
		print("Congrats! You win!!!")
	if what_happened=="computer_wins":
		print("PC won")
	if what_happened=="deck_finished":
		ch=len(computer_hand)
		hh=len(human_hand)
		print("Deck is empty ! PC has", ch, "cards and player has", hh)
	if ch>hh:
		print("Congrats You Won")
	if ch<hh:
		print("PC won")
	if ch==hh: 
		print("Draw")
	print()







def next_turn():
	global what_happened
	while True:
		if what_happened=="game_start":
			initial()
		elif what_happened=="human_played":
			if len(human_hand)==0:
				what_happened="human_wins"
				evaluate()
				break
			print()
			print("--------------PC turn ------------")
			print()
			computer_plays()
		elif what_happened=="computer_played":
			if len(computer_hand)==0:
				what_happened="computer_wins"
				evaluate()
				break
			print()
			print("--------------Player's turn--------")
			human_plays()
		elif what_happened=="deck_finished":
			evaluate()
			break

print("Game With Cards 1.0")
print("===================")
print()

#Global variables

d=deck()
table=[]
computer_hand=[]
human_hand=[]
what_happened=""

again="y"
while again=="y":
	what_happened="game_start"
	next_turn()
	print("Do you want to play again")
	again=input("write y or n: ")
print("GAME ENDS")