def numToWords():
	a=0
    if int(num) == 0:
    	print("zero")
    elif len(num) > 7:
    	print("Input out of bounds! Enter a number from 0-1000000")
    else: 
	    for i in range (0,len(num)):
	    	if i==len(num)-1 or i==len(num)-3 or i==len(num)-4 or i==len(num)-6 or i==len(num)-7:
	    		if a==1:
	    			a=0
	    			continue
	    		if num[i] == "1":
	    			print("one ", end="")
	    		elif num[i] == "2":
	    			print("two ", end="")
	    		elif num[i] == "3":
	    			print("three ", end="")
	    		elif num[i] == "4":
	    			print("four ", end="")
	    		elif num[i] == "5":
	    			print("five ", end="")
	    		elif num[i] == "6":
	    			print("six ", end="")
	    		elif num[i] == "7":
	    			print("seven ", end="")
	    		elif num[i] == "8":
	    			print("eight ", end="")
	    		elif num[i] == "9":
	    			print("nine ", end="")
	    		if (i==len(num)-3 or i==len(num)-6) and num[i]!="0":
	    			print("hundred ", end="")
	    		elif i==len(num)-4 and num[i]!="0":
	    			print("thousand ", end="")
	    		elif i==len(num)-7:
	    			print("million ", end="")
	    	elif i==len(num)-2 or i==len(num)-5:
	    		if num[i] =="1":
	    			a = 1
	    		if num[i] == "1" and num[i+1] == "0":
	    			print("ten ", end="")
	    		elif num[i] == "1" and num[i+1] == "1":
	    			print("eleven ", end="")
	    		elif num[i] == "1" and num[i+1] == "2":
	    			print("twelve ", end="")
	    		elif num[i] == "1" and num[i+1] == "3":
	    			print("thirteen ", end="")
	    		elif num[i] == "1" and num[i+1] == "4":
	    			print("fourteen ", end="")
	    		elif num[i] == "1" and num[i+1] == "5":
	    			print("fifteen ", end="")
	    		elif num[i] == "1" and num[i+1] == "6":
	    			print("sixteen ", end="")
	    		elif num[i] == "1" and num[i+1] == "7":
	    			print("seventeen ", end="")
	    		elif num[i] == "1" and num[i+1] == "8":
	    			print("eighteen ", end="")
	    		elif num[i] == "1" and num[i+1] == "9":
	    			print("nineteen ", end="")
	    		elif num[i] == "2":
	    			print("twenty ", end="")
	    		elif num[i] == "3":
	    			print("thirty ", end="")
	    		elif num[i] == "4":
	    			print("forty ", end="")
	    		elif num[i] == "5":
	    			print("fifty ", end="")
	    		elif num[i] == "6":
	    			print("sixty ", end="")
	    		elif num[i] == "7":
	    			print("seventy ", end="")
	    		elif num[i] == "8":
	    			print("eighty ", end="")
	    		elif num[i] == "9":
	    			print("ninety ", end="")
	    		if i==len(num)-5 and (num[i]=="1" or num[i+1]=="0"):
	    			print("thousand ", end="")

	    print("\n")	
'''
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

