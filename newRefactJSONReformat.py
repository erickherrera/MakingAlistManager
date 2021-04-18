import json
from difflib import SequenceMatcher

# costume class
from newCopyRefact import xslToJson

class ReFormatJson:

	def __init__(self,headers,content):
		# main globals
		self.headers = headers
		self.content = content
		# headers global
		self.namesToFind = ['name','full name','username','first name']
		self.lastnamesToFind = ['last name','lastname','surname']
		self.address = ["addres","Street Address","full addres","city","state","zip","zip code","area code"]
		self.mobilePhonesToFind =['phone','cell','number']
		self.LandlineToFindIn =['landline']
		self.EmailsToFindIn = ['email','emails']
		self.mailAdressToFind = ['Mail Street Address','Mail','full Mail','mail address','Mail City','Mail State','Mail zip']

		# list holding fomat results
		self.finalList = []


	# find similar strings function
	def similar(self,a, b):
		headername = a.lower()
		headerNameFromSL = b.lower()
		return SequenceMatcher(None,headername,headerNameFromSL).ratio()

	def saveToList(self,content):
		theCopy= content.copy()
		self.finalList.append(theCopy)

	def giveBackFinalList(self):
		return self.finalList

	def saveToFile(self):
		makeString = str(self.finalList)
		with open('end.json', 'w') as json_file:
			json.dump(makeString, json_file)

	# I will find The headers for the new Json
	def findHeadersToReformat(self):
		finishObject = {}
		for eachObjactFromContent in range(len(self.content)):
			for headerPositionNumber in range(len(self.headers)):
				for theNamesToFindValue in self.namesToFind:
					if self.similar(theNamesToFindValue,self.headers[headerPositionNumber]) == 1.0:
						finishObject['name'] = self.content[eachObjactFromContent][self.headers[headerPositionNumber]]

			for headerPositionNumber in range(len(self.headers)):
				for thelastNamesToFindValue in self.lastnamesToFind:
					if self.similar(thelastNamesToFindValue,self.headers[headerPositionNumber]) == 1.0:
						finishObject['Last Name'] = self.content[eachObjactFromContent][self.headers[headerPositionNumber]]

			AddresBox = []
			for headerOfAddress in range(len(self.headers)):
				for addresDetailsToFind in self.address:
					if self.similar(addresDetailsToFind,self.headers[headerOfAddress]) == 1.0:
						AddresBox.append(self.content[eachObjactFromContent][self.headers[headerOfAddress]])
			finishObject['Full Adress'] = AddresBox

			mobilePhone = []
			for headerForMobile in range(len(self.headers)):
				for findMobile in self.mobilePhonesToFind:
					divider =  self.headers[headerForMobile].split(" ")
					if self.similar(findMobile,divider[0]) == 1.0:
						if self.content[eachObjactFromContent][self.headers[headerForMobile]]!= "null":
							mobilePhone.append(self.content[eachObjactFromContent][self.headers[headerForMobile]])
			if len(mobilePhone) > 0:
				finishObject['Mobile'] = mobilePhone

			emailsbox = []

			for headerForEmail in range(len(self.headers)):
				for findEmails in self.EmailsToFindIn:
					divider =  self.headers[headerForEmail].split(" ")
					if self.similar(findEmails,divider[0]) == 1.0:
						if self.content[eachObjactFromContent][self.headers[headerForEmail]]!= "null":
							emailsbox.append(self.content[eachObjactFromContent][self.headers[headerForEmail]])
			if len(emailsbox) > 0:
				finishObject['Emails'] = emailsbox

			landlinebox = []

			for headerForLandline in range(len(self.headers)):
				for findLandline in self.LandlineToFindIn:
					divider =  self.headers[headerForLandline].split(" ")
					if self.similar(findLandline,divider[0]) == 1.0:
						if self.content[eachObjactFromContent][self.headers[headerForLandline]]!= "null":
							landlinebox.append(self.content[eachObjactFromContent][self.headers[headerForLandline]])

			if len(landlinebox) > 0:
				finishObject['landLine'] = landlinebox

			MailAddresBox = []

			for headerOfMailAddress in range(len(self.headers)):
				for MailaddresDetailsToFind in self.mailAdressToFind:
					if self.similar(MailaddresDetailsToFind,self.headers[headerOfMailAddress]) == 1.0:
						MailAddresBox.append(self.content[eachObjactFromContent][self.headers[headerOfMailAddress]])
			if len(MailAddresBox) > 0:
				finishObject['Mail Address'] = MailAddresBox
				
			finishObject['sms'] = "false"
			self.saveToList(finishObject)

# done  ....