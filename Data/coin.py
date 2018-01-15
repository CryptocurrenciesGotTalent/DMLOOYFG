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
		lines = open(os.path.abspath(__file__ + "/../CoinsData/"+self.name+".txt"), "r").readlines()
		for line in lines:
			data = line.split(";")
			if dateToString(dd,mm,yyyy) == data[0]:
				return Candle(float(data[1]), float(data[2]), float(data[3]), float(data[4]))

		raise ValueError("could not retrieve data for " + self.name + " at date " + dateToString(dd,mm,yyyy))


	def getMarketCapAt(self, dd, mm, yyyy):
		lines = open(os.path.abspath(__file__ + "/../CoinsData/"+self.name+".txt"), "r").readlines()
		for line in lines:
			data = line.split(";")
			if dateToString(dd,mm,yyyy) == data[0]:
				return float(data[6])

		raise ValueError("could not retrieve data for " + self.name + " at date " + dateToString(dd,mm,yyyy))
