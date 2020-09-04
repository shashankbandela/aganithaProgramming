import sys, os

def initialize() :
	###### READING CURRENCIES FROM DEFINED LIBRARY AND STROING THEM IN ARRAY #########
	with open('currency-lib.txt', 'r') as f :
		s = f.read() 
	s = s.split('\n')
	global currency
	currency = []
	for i in range(len(s) - 1) :
		l = s[i].split()
		currency.append(l)

	#print (currency)
	f.close()

	###### READING NUMBERS FROM DEFINED LIBRARY AND STROING THEM IN ARRAY #########
	with open('numbers-lib.txt', 'r') as f :
		s = f.read() 
	s = s.split('\n')
	global numbers
	numbers = []
	for i in range(len(s) - 1) :
		l = s[i].split()
		numbers.append(l)

	#print (numbers)
	f.close()


def convertCurrency(line) :
	words = line.split()
	out = ''
	i = 0
	while i < len(words) - 1:
		print (i)
		found = 0
		found2 = 0
		for num in numbers :
			if words[i] == num[0] :
				found = 1
				numm = num[1]
				break
		if found == 1 :
			for cur in currency :
				if (words[i+1] == cur[1]) | (words[i+1] == cur[0]) :
					curr = cur[2]
					found2 = 1
					break
		if found2 == 1 :
			out += str(curr) + str(numm) + ' '
			i += 1	

		else :
			out += words[i] + ' ' 
		
		i += 1
	return out + '\n'
				
			
def convertText(line) :
	#### WE CALL ALL THE NECESSARY CONVERSIONS HERE #########
	### IMPLEMENTED ONLY CURRENCY CONVERTOR ######

	newLine = convertCurrency(line)

	return newLine	

def main():
	###### OPENING FILE #######
	try :
		para = open(sys.argv[1], 'r') 
	except :
		print("Error opening file")
		return 
	##### READING LINE ########	
	lines = para.readlines() 

	####### INITIALIZING THE SETUP #########
	initialize()

	##### OUTPUT FILENAME #########
	filename, file_extension = os.path.splitext(sys.argv[1])
	outfile = filename + '-converted' + file_extension


	######### WRITING TO NEWFILE #######
	out = open(outfile, 'w')
	for line in lines :
		line = convertText(line)
		out.write(line)


	para.close()
	out.close()


if __name__=="__main__":
    main()
