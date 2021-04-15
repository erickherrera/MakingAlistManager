import json
from difflib import SequenceMatcher

# costume class
from newCopyRefact import xslToJson



# global variables
matchingHeadersFromJsonList = []

# find similar strings function
def similar(a, b):
	headername = a.lower()
	headerNameFromSL = b.lower()
	return SequenceMatcher(None,headername,headerNameFromSL).ratio()


# I will find The headers for the new Json
def findHeadersToReformat(headers,content):
	# find Name or full name
	print("waiting for code...")





load = xslToJson("me.xlsx")

headersGiver = load.giveHeadersBack()
valueFromContent =  load.giveValueBack()

findHeadersToReformat(headersGiver,valueFromContent)