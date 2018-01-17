import os

def dateToString(dd, mm, yyyy):
	return ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][mm-1]+ " " + str(dd).zfill(2)+" "+str(yyyy)



class Candle:
	def __init__(self, OPEN, HIGH, LOW, CLOSE):
		self.OPEN = OPEN
		self.HIGH = HIGH
		self.LOW = LOW
		self.CLOSE = CLOSE



class Coin:
	def __init__(self, name):
		self.name = name

	def getCandleAt(self, dd, mm, yyyy):
		lines = open(os.path.abspath(__file__ + "/../../Data/CoinsData/"+self.name+".txt"), "r").readlines()
		for line in lines:
			data = line.split(";")
			if dateToString(dd,mm,yyyy) == data[0]:
				return Candle(float(data[1]), float(data[2]), float(data[3]), float(data[4]))

		raise None


	def getMarketCapAt(self, dd, mm, yyyy):
		lines = open(os.path.abspath(__file__ + "/../../Data/CoinsData/"+self.name+".txt"), "r").readlines()
		for line in lines:
			data = line.split(";")
			if dateToString(dd,mm,yyyy) == data[0] and float(data[6]) != 0.0:
				return float(data[6])

		return None

	
	def getPriceVariation(self, initialDate, finalDate, priceType):
		dd1, mm1, yyyy1 = initialDate
		dd2, mm2, yyyy2 = finalDate

		if self.getCandleAt(dd1, mm1, yyyy1).OPEN != None:
			if (priceType == 'OPEN'):
				initialPrice = self.getCandleAt(dd1, mm1, yyyy1).OPEN
				finalPrice = self.getCandleAt(dd2, mm2, yyyy2).OPEN
			elif (priceType == 'HIGH'):
				initialPrice = self.getCandleAt(dd1, mm1, yyyy1).HIGH
				finalPrice = self.getCandleAt(dd2, mm2, yyyy2).HIGH
			elif (priceType == 'LOW'):
				initialPrice = self.getCandleAt(dd1, mm1, yyyy1).LOW
				finalPrice = self.getCandleAt(dd2, mm2, yyyy2).LOW
			elif (priceType == 'CLOSE'):
				initialPrice = self.getCandleAt(dd1, mm1, yyyy1).CLOSE
				finalPrice = self.getCandleAt(dd2, mm2, yyyy2).CLOSE			

			return finalPrice/initialPrice
		
		return None

	def getMarketCapVariation(self, initialDate, finalDate):
		dd1, mm1, yyyy1 = initialDate
		dd2, mm2, yyyy2 = finalDate

		if self.getMarketCapAt(dd1, mm1, yyyy1) != None:
			if self.getMarketCapAt(dd2, mm2, yyyy2) == None:
				return 0
			return self.getMarketCapAt(dd2, mm2, yyyy2)/self.getMarketCapAt(dd1, mm1, yyyy1)

		return None