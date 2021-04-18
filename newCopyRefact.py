import pandas as pd
import json
from string import digits

class xslToJson:
	def __init__(self,nameFile):
		self.obj ={}
		self.a_list = []
		self.objectCreatedForJsonFileFromHeaders = [];
		self.df = pd.read_excel(nameFile, engine="openpyxl")
		self.getHeaders()
		self.makeObjectsUsingHeaders()

	def saveDataToFile(self,content):
		theCopy= content.copy()
		self.a_list.append(theCopy)

	def getHeaders(self):
		for Y in range(len(self.df.columns)):
			self.objectCreatedForJsonFileFromHeaders.insert(Y,self.df.columns[Y])

	def makeObjectsUsingHeaders(self):
		for x in range(len(self.df[self.objectCreatedForJsonFileFromHeaders[0]])):
			for headerName in self.objectCreatedForJsonFileFromHeaders:
				if pd.isna(self.df[headerName][x]):
					self.obj[headerName] = "null"
				else:
					self.obj[headerName] = self.df[headerName][x]
			self.saveDataToFile(self.obj)

	# giving values back for Use...
	def giveValueBack(self):
		# makeString = str(self.a_list)
		return self.a_list

	def giveHeadersBack(self):
		return self.objectCreatedForJsonFileFromHeaders

	def saveToFile(self):
		makeString = str(self.a_list)
		with open('data.json', 'w') as json_file:
			json.dump(makeString, json_file)


# done.......












