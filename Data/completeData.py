import os
from functools import reduce

def fillMarketCap(fileName):
	file = open("data/"+fileName, 'r')
	contentTable = list(map(lambda line:line.strip().split(";"), file.readlines()))

	#find a line with available data
	goodLine = []
	found = False
	for line in contentTable:
		found = reduce(lambda x,y:x and y, [s != '-' for s in line])
		print(found)
		if found :
			goodLine = line
			break
			
		if(not found):
			print("alors la ..." + os.getcwd()+"/data/"+fileName)
			file.close()
			os.remove(os.getcwd()+"/data/"+fileName)


# #use goodLine Data to fill missing market caps
# 	supply = float(goodLine[6])/float(goodLine[1])
# 	for i in range(len(contentTable)):
# 		line = contentTable[i]
# 		if line[6] == '-' and line[1] != '-':
# 			#find a close available MC
# 			# if(i>0):
# 			# 	goodLine = contentTable[i-1]
# 			# 	supply = float(goodLine[6])/float(goodLine[1])
# 			# contentTable[i][6] = str(float(line[1])*supply)
# 	with open("filledMCdata/" + fileName, 'w') as newFile:
# 		for line in contentTable:
# 			newFile.write(reduce(lambda x,y:x+";"+y, line) + "\n")



for fileName in os.listdir(os.getcwd()+"/data"):
	try:
		fillMarketCap(fileName)
	except:
		print("hahaha")
		pass