from directionalReturn import directionalReturn
from AW_API import weather
from grouping import severity

start = input("Please enter the city and state you are traveling from, separated by a comma: ")
start.rstrip()
start.lstrip()
end = input("Please enter the city and state you are traveling to, separated by a comma: ")
end.rstrip()
end.lstrip()

totalList = directionalReturn(start, end)

for list in totalList:
	answer = weather(list[0[0]],list[0[1]])
	print(answer)