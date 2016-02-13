'''
def numToWords():

def wordsToNum():
	
def wordsToCurrency():
'''
def numberDelimited():
	s = input("Input: ")

	inQuotes = False
	current = ""
	results = []
	currentQuote = ""
	for c in s:
	    if not inQuotes and c == ",":
	        results.append(current)
	        current = ""
	    elif not inQuotes and (c == '"' or c == "'"):
	        currentQuote = c
	        inQuotes = True
	    elif inQuotes and c == currentQuote:
	        currentQuote = ""
	        inQuotes = False
	    else:
	        current += c

	results.append(current)

	if len(results) != 3:
		print("Invalid Input!")

	else:
		length = len(results[0])
		length -= int(results[2])
		print(results[0][:length] + results[1] + results[0][length:])

