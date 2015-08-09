# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function
def rotate_word(word,number):
	newword = ""
	#Loop through the word
	for c in word: 
		#Check if the character is upper case or lower case
		if c.islower():
			case = True
		else:
			case = False
		#Change character to ASCII value
		ascii = ord(c)
		#Increment by number. Remember to check for border values; z + 1 = a, a - 1 = z
		#A-Z = 65-90, a-z = 97-122
		newascii = ascii + number
		if newascii > 90 and case == False:
			# Character is uppercase, rotate to uppercase character
			newascii = newascii - 90 + 64
		elif newascii < 65 and case == False:
			#Character is uppercase, rotate to uppercase character
			newascii = 91 - (65 - newascii)
		elif newascii > 122 and case == True:
			# Character is lowercase, rotate to lowercase character
			newascii = newascii - 122 + 96
		elif newascii < 97 and case == True:
			# Character is lowercase, rotate to lowercase character
			newascii = 123 - (97 - newascii)
		#Convert numeric ASCII value to character
		c = chr(newascii)
		#Append character to new word
		newword = "".join((newword,c))
	return newword

def main():
	print rotate_word('cheer',7)
	print rotate_word('Cheer',7)
	print rotate_word('melon',-10)
	print rotate_word('Melon',-10)

if __name__ == '__main__':
    main()