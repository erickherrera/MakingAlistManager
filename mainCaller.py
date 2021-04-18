# costume Scripts
from newCopyRefact import xslToJson
from newRefactJSONReformat import ReFormatJson

# send file to get json..
load = xslToJson("me2.xlsx")

# get values back
headersGiver = load.giveHeadersBack()
valueFromContent =  load.giveValueBack()

# reformat values 
formatingJson = ReFormatJson(headersGiver,valueFromContent)
formatingJson.headFinderManager()

# if you wanna save end result use function 
# formatingJson.saveToFile()

# end... show results.....
print(formatingJson.giveBackFinalList())
