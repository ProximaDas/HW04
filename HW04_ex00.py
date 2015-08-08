#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def guess_random(x):
	# Ask user for input
	input = raw_input("Guess what number I chose (Hint: It's between 1 and 25): ")
	try:
		number = int(input)
	except:
		print "I'm afraid that's not a number. Try again."
	else:
		if number == x:
			print ("You've read my mind! That is the number I chose.")
			return True
		elif number > x:
			print ("Aiming too high, mate.My guess is lower than that.")
			return False
		else:
			print ("Aiming too low, my friend. My guess is higher than that.")
			return False



################################################################################
def main():
	# Generate a random integer between 1 and 25
	random_int = random.randint(1,25)
	# Set a counter
	counter = 1
	while True:
		result = guess_random(random_int)
		if result == True:
			break
		else:
			# Increment the counter
			counter += 1
			# Check the counter
    		if counter <= 5:
    			continue
    		else:
    			print "You've tried 5 times. Better luck next time!"
    			break
    			

if __name__ == '__main__':
    main()