import random
class card():
	def __init__(self,val,sym):
		self.value=val
		self.symbol=sym
		if self.symbol in "sc": 
			self.color='B'
		else:
			self.color='R'

		if self.value in "JQK":
			self.fig=True
		else:
			self.fig=False

	def __str__(self):
		return self.value+self.symbol

	def detailed_info(self):
		print("Value: ", self.value, "Symbol: ", self.symbol)
		print("Color: ", self.color, "Figure: ", self.fig)


class deck():
	values="A23456789TJQK"
	symbols="shcd"

	def __init__(self):
		self.content=[] #cards in deck
		self.pile=[]	#cards out of deck

		for s in deck.symbols:
			for v in deck.values:
				c=card(v,s)
				self.content.append(c)

	def __str__(self):
		s=""
		cntr=0
		for i in self.content:
			s=s+str(i)+ " "
			cntr=cntr+1
			if(cntr%13==0):
				s=s+'\n'
		if s[-1]!='\n': 
			s=s+'\n'

		s=s+str(len(self.content))+"-"+str(len(self.pile))

	def shuffle(self):
		random.shuffle(self.content)

	def draw(self):
		if len(self.content)<1:
			return "empty"
		c=self.content[0]
		self.content=self.content[1:]
		self.pile.append(c)
		return c

	def collect(self):
		self.content=self.content+self.pile
		self.pile=[]
		

