#Import the functions we need from four of our other files
from directionalReturn import directionalReturn
from AW_API import weather
from grouping import severity
from pathWeight import weight

#Grab the user's starting and ending location, stripping leading/trailing spaces
'''
start = input('\nPlease enter the address you are traveling from: ')
start.rstrip()
start.lstrip()
end = input('\nPlease enter the address you are traveling to: ')
end.rstrip()
end.lstrip()
'''
def main(start="",end=""):

	#Using the defined start/end points, generate the best geographic route from start to end
	totalList = directionalReturn(start, end)
	print(totalList)
	'''
		Since totalList contains full lat/lng coordinates for every turn on the route,
		as well as the time data for those locations, we need to look at the nested dictionaries,
		taking the first dictionary in every nested list and running the weather() and severity()
		functions over them.
	'''
	for lists in range(len(totalList)):
		answer = weather(totalList[lists][0])
		severe = severity(answer)
		print(severe)
		totalList[lists][0]= severe
	print(totalList)

	'''
		Taking the severity from totalList, we then apply our own weight based
		off preassigned weighted weather values, and return a response as to
		if the user should delay or not based off the weighted value.
	'''
	MainWaitTime = weight(totalList)
	print(MainWaitTime)

	FinalVALUE = MainWaitTime.index(min(MainWaitTime))
	if(FinalVALUE==0):
		print("The best time for you to leave for " +str(end)+" would be now.")
	else:
		print("The best time for you to leave for " +str(end)+" would be in "+str(FinalVALUE)+" hour"+ ("s"if FinalVALUE>1 else ""))
	return FinalVALUE