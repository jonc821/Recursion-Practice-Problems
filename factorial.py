def factorial(number):
	
	# Terminating Case
	if number == 0:
		return 1
	
	# Recursive Call	
	return number * factorial(number - 1)
	
def number_input(question):
	answer = raw_input(question)
	
	if answer.isdigit():
		return int(answer)
		
	return number_input("Numbers only please! Try again. ")
	

################# Main Program Below

userNumber = number_input("Give me a number: ")
userFactorial = factorial(userNumber)
print("The factorial of your number is: ")
print(userFactorial)



