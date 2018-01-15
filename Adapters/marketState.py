import os
from coin import *


class MarketState:
	def __init__(self, dd, mm, yyyy):
		self.day = dd
		self.month = mm
		self.year = yyyy
		self.dateString = dateToString(dd,mm,yyyy)
		self.data = open(os.path.abspath(__file__ + "/../../Data/CoinsDataByDate/"+self.dateString+".txt"), "r").readlines()


	def getCoinAtRank(self, i):

		if(i>len(self.data)):
			raise ValueError("invalid rank : too big")

		return Coin(self.data[i-1].split(";")[0])


	def getMarketCapAtRank(self, i):

		if(i>len(self.data)):
			raise ValueError("invalid rank : too big")

		return float(self.data[i-1].split(";")[6])


	def getTotalMarketCap(self):

		return sum([self.getMarketCapAtRank(i) for i in range(1, len(self.data)+1)])



