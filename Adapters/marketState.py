import os
from Adapters.coin import *


class MarketState:
	def __init__(self, dd, mm, yyyy):
		self.day = dd
		self.month = mm
		self.year = yyyy
		self.dateString = dateToString(dd,mm,yyyy)
		self.data = open(os.path.abspath(__file__ + "/../../Data/CoinsDataByDate/"+self.dateString+".txt"), "r").readlines()

	def getNbCoins(self):
		return len([line for line in self.data if line.strip()])


	def getCoinAtRank(self, i):

		if(i>len(self.data)):
			raise ValueError("invalid rank : too big")

		return Coin(self.data[i-1].split(";")[0])


	def getMarketCapAtRank(self, i):

		if(i>len(self.data)):
			raise ValueError("invalid rank : too big")

		return float(self.data[i-1].split(";")[6])


	def getPriceAtRank(self, i, priceType):

		if(i>len(self.data)):
			raise ValueError("invalid rank : too big")
		else:
			if (priceType == 'OPEN'):
				price = self.data[i-1].split(";"[1])
			elif (priceType == 'HIGH'):
				price = self.data[i-1].split(";"[2])
			elif (priceType == 'LOW'):
				price = self.data[i-1].split(";"[3])
			elif (priceType == 'CLOSE'):
				price = self.data[i-1].split(";"[4])

		return price

	def getTotalMarketCap(self):

		return sum([self.getMarketCapAtRank(i) for i in range(1, len(self.data)+1)])




