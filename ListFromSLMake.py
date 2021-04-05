import pandas as pd
import json

# global shit.. 
obj ={}
a_list = []
objectCreatedForJsonFileFromHeaders = [];

def saveDataToFile(content):
	theCopy= content.copy()
	a_list.append(theCopy)
				
def getHeaders(df):
	for Y in range(len(df.columns)):
		objectCreatedForJsonFileFromHeaders.insert(Y,df.columns[Y])

def makeObjectsUsingHeaders(df):
	for x in range(len(df[objectCreatedForJsonFileFromHeaders[0]])):
		for headerName in objectCreatedForJsonFileFromHeaders:
			if pd.isna(df[headerName][x]):
				obj[headerName] = "null"
			else:
				obj[headerName] = df[headerName][x]
			
		objectToJsonFormat = []
		saveDataToFile(obj)

def lastStep():
	makeString = str(a_list)
	backTOJson = json.dumps(makeString)
	load = json.loads(backTOJson)
	changeQuotes = load.replace('\'','"')

	f = open("notes.json", "w")
	f.write(changeQuotes)
	f.close() 

def nameTheUNName(fileName):
	df = pd.read_excel(fileName, engine="openpyxl")
	getHeaders(df)
	makeObjectsUsingHeaders(df)
	lastStep()




# just give me the name of the xlsx file to strip data from it
nameTheUNName("me.xlsx")












