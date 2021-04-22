# costume Scripts
from newCopyRefact import xslToJson
from newRefactJSONReformat import ReFormatJson

#Function to check phone number  \

def findContactViaPhone(str):
    try:
        if(len(phoneInput) >= 7 and int(phoneInput)):
            for x in range (len(finalJSON)):

                print(finalJSON[x]['Mobile'])
                
    except:
        print('Please enter a complete phone number')    

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

finalJSON = formatingJson.giveBackFinalList()
print(type(finalJSON))



phoneInput = input("Search Phone Number including the area code: ")
findContactViaPhone(phoneInput)



