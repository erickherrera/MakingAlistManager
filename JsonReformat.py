import json
from difflib import SequenceMatcher

# costume class
from newCopyRefact import xslToJson



# global variables
matchingHeadersFromJsonList = []

# find similar strings function
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# I will find The headers for the new Json
def findHeadersToReformat(headers,content):

	print(headers[0])
	print(content[1]['First Name'])




load = xslToJson("me.xlsx")

headersGiver = load.giveHeadersBack()
valueFromContent =  load.giveValueBack()

findHeadersToReformat(headersGiver,valueFromContent)