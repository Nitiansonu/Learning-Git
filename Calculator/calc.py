# Defining class

class calculator:
	def userInput():
		x = raw_input("Enter first number :")
		y = raw_input("Enter second number :")
		return [x,y]
		

if "__name__"=="__main__":
	app = calculator()
	app.userInput()
