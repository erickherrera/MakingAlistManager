import json
from difflib import SequenceMatcher

# costume class
from newCopyRefact import xslToJson



# global variables
matchingHeadersFromJsonList = []
finalList = []


# find similar strings function
def similar(a, b):
	headername = a.lower()
	headerNameFromSL = b.lower()
	return SequenceMatcher(None,headername,headerNameFromSL).ratio()




def saveToList(content):
	theCopy= content.copy()
	finalList.append(theCopy)

# I will find The headers for the new Json
def findHeadersToReformat(headers,content):
	# object blue print....
	finishObject = {}

	# find Name or full name
	namesToFind = ['name','full name','username','first name']
	print("Re Formating....")
	print("................")
	

	for eachObjactFromContent in range(len(content)):
		# name finder
		for headerPositionNumber in range(len(headers)):
			for theNamesToFindValue in namesToFind:
				if similar(theNamesToFindValue,headers[headerPositionNumber]) == 1.0:
					finishObject['Name'] = content[eachObjactFromContent][headers[headerPositionNumber]]


		lastnamesToFind = []


		mobilePhonesToFind =[]


		landlineToFind =[]


		emailsToFind = []



		saveToList(finishObject)



load = xslToJson("me2.xlsx")

headersGiver = load.giveHeadersBack()
valueFromContent =  load.giveValueBack()

findHeadersToReformat(headersGiver,valueFromContent)




# finalList has all the reformated content
