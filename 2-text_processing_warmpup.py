import sys
import re

stdin = sys.stdin.readlines()

def count_a(text):
	pattern = "[ ]{1,2}[aA]{1}[ ]{1,2}"
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_an(text):
	pattern = "[ ]{1,2}[aA]{1}[n]{1}[ ]{1,2}"
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_the(text):
	pattern = "([ ,?.!\'\"]{1,2}[t]{1}|[T]{1})[h]{1}[e]{1}[ ]{1,2}"
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_dates(text):
	def count_allnumeric():
		# month day year
		pattern = "[0-9]{1,2}[ \.\-_/]{1}[0-9]{1,2}[ \.\-_/]{1}[0-9]{2,4}"
		results = re.findall(pattern, text)
		count = len(results)
		return(count)
	
	def count_allwords():
		# day month year
		pattern = "[0-9]{1,2}[thrdns]{0,2}[ ]{1,2}[a-zA-Z]{3,9}[ \-,]{1,2}[0-9]{2,4}"
		results = re.findall(pattern, text)
		count = len(results)
		return(count)

	def count_allwords2():
		# month day year
		pattern = "[a-zA-Z]{3,9}[ ,]{1,2}[0-9]{1,2}[ ,]{1,2}[0-9]{2,4}"
		results = re.findall(pattern, text)
		count = len(results)
		return(count)
	
	total_count = count_allnumeric() + count_allwords() + count_allwords2()
	return(total_count)


# Get arguments using stdin
N = int(stdin[0])
for i in range(2*N)[1::]:
	# Cycle through each actual text
	if (i % 2) != 0:
		text = stdin[i]
		# Print results for each function
		print(count_a(text))
		print(count_an(text))
		print(count_the(text))
		print(count_dates(text))