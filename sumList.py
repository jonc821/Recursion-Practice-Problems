def sum_list(listofNumbers):
	if len(listofNumbers) == 0:
		return 0
	
	return listofNumbers[0] + sum_list(list[1:])
	
######### Main Program Below #########
listOfNumbers = [1, 3, 5, 7, 9]
print(sum(listOfNumbers))

 