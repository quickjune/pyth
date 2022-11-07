# Find Factorial of a number using Recursion

# Define Number whose Factorial to be calculated
num = 6      
      
def factorial(num):
	# single line to find factorial
	return 1 if (num==1 or num==0) else num * factorial(num - 1);

print("Factorial of",num,"is", factorial(num))
