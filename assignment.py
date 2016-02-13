def numToWords():
    num = input("Enter a number: ")

    a=0
    if int(num) == 0:
    	print("zero")
    elif len(num) > 7:
    	print("Input out of bounds! Enter a number from 0-1000000")
    else: 
	    for i in range (0,len(num)):
	    	if i==len(num)-1 or i==len(num)-3 or i==len(num)-4 or i==len(num)-6 or i==len(num)-7:
	    		if a==1:
	    			a=0 #for checking if eleven-nineteen has already been printed
	    			continue #if yes, units must not be printed anymore
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

def wordsToNum():
	num = input("Enter a number (in words): ")
	convert(num)

def convert(num): #function for converting words into number form
	number = 0
	temp = 0 #temporary variable for computation
	if num == "zero":
		print("0")
	else: 
		s = num.split(" ") #put all words in a list
		for i in range (0,len(s)):
			if s[i] == "one":
				temp+=1
			elif s[i] == "two":
				temp+=2
			elif s[i] == "three":
				temp+=3
			elif s[i] == "four":
				temp+=4
			elif s[i] == "five":
				temp+=5
			elif s[i] == "six":
				temp+=6
			elif s[i] == "seven":
				temp+=7
			elif s[i] == "eight":
				temp+=8
			elif s[i] == "nine":
				temp+=9
			elif s[i] == "ten":
				temp+=10
			elif s[i] == "eleven":
				temp+=11
			elif s[i] == "twelve":
				temp+=12
			elif s[i] == "thirteen":
				temp+=13
			elif s[i] == "fourteen":
				temp+=14
			elif s[i] == "fifteen":
				temp+=15
			elif s[i] == "sixteen":
				temp+=16
			elif s[i] == "seventeen":
				temp+=17
			elif s[i] == "eighteen":
				temp+=18
			elif s[i] == "nineteen":
				temp+=19
			elif s[i] == "twenty":
				temp+=20
			elif s[i] == "thirty":
				temp+=30
			elif s[i] == "forty":
				temp+=40
			elif s[i] == "fifty":
				temp+=50
			elif s[i] == "sixty":
				temp+=60
			elif s[i] == "seventy":
				temp+=70
			elif s[i] == "eighty":
				temp+=80
			elif s[i] == "ninety":
				temp+=90
			elif s[i] == "hundred":
				temp*=100
			elif s[i] == "thousand":
				temp*=1000
				number+=temp
				temp=0
			elif s[i] == "million":
				temp*=1000000
				number+=temp
				temp=0
			if i==len(s)-1: #if index is already for the last word in the list
				number+=temp #put temp to number
		print(number)

def wordsToCurrency():
	inp = input("Input: ")
	s = inp.split(",") #splits the string by ',' then puts it in a list

	print(s[1].replace("'", ""), end="") #replace all occurences of an apostrophe for the currency; prints the new string
	convert(s[0].replace("'", "")) #replace all occurences of an apostrophe for the word; converts the new string to number form

def numberDelimited():
	s = input("Input: ")

	inQuotes = False
	current = ""
	args = []
	currentQuote = ""

	for c in s: #extracts all characters that are not ''','"', or ',' then puts them in the list called "args"
	    if not inQuotes and c == ",":
	        args.append(current)
	        current = ""
	    elif not inQuotes and (c == '"' or c == "'"):
	        currentQuote = c
	        inQuotes = True
	    elif inQuotes and c == currentQuote:
	        currentQuote = ""
	        inQuotes = False
	    else:
	        current += c

	args.append(current)

	if len(args) != 3: #if the number of arguments entered by the user is not equal to 3
		print("Invalid Input!")

	else:
		length = len(args[0])
		length -= int(args[2]) #subtracts the number of jumps from the length of the first number entered
		print(args[0][:length] + args[1] + args[0][length:]) #puts the 2nd argument (the delimiter) after the index of the new length

