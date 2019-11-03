from directionalReturn import directionalReturn
from AW_API import weather
from grouping import severity
from pathWeight import weight

start = input("Please enter the city and state you are traveling from, separated by a comma: ")
start.rstrip()
start.lstrip()
end = input("Please enter the city and state you are traveling to, separated by a comma: ")
end.rstrip()
end.lstrip()

totalList = directionalReturn(start, end)

for lists in range(len(totalList)):
	answer = weather(totalList[lists][0])
	severe = severity(answer)
	totalList[lists][0]= severe

#print(totalList)


MainWaitTime = weight(totalList)
#print(MainWaitTime)


FinalVALUE = MainWaitTime.index(min(MainWaitTime))
if(FinalVALUE==0):
	print("The best time for you to leave for " +end+" would be now.")
else:
	print("The best time for you to leave for " +end+" would be in "+FinalVALUE+" hour"+ ("s"if FinalVALUE>1 else ""))
print(FinalVALUE)