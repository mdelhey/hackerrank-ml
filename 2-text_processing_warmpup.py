import sys
import re

def count_a(text):
	pattern = "[ ]{1,2}[aA]{1}[ ]{1,2}"
	# Grab results, count them, return.
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_an(text):
	pattern = "[ ]{1,2}[aA]{1}[n]{1}[ ]{1,2}"
	# Grab results, count them, return.
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_the(text):
	pattern = "[ ]{1,2}[tT]{1}[h]{1}[e]{1}[ ]{1,2}"
	# Grab results, count them, return.
	results = re.findall(pattern, text)
	count = len(results)
	return(count)

def count_dates(text):
	# mdy or dmy
	def count_allnumeric():
		pattern = "[ ]{1,2}[1-9]{1,2}[./- _]{0,1}[1-9]{1,2}[./- _]{0,1}[1-9]{2,4}"
		results = re.findall(pattern, text)
		count = len(results)
		return(count)
	
	#def count_allwords():
		#pattern = "[1-9]+[th|rd|st}[ ]{1,2}[a-zA-z]+"
		#results = re.findall(pattern, text)
		#count = len(results)
		#return(count)
	
	#total_count = count_allnumeric() + count_allwords()
	total_count = count_allnumeric()
	return(total_count)

#text = "New York is a state in the Northeastern region of the United States. New York is the 27th-most extensive, the 3rd-most populous, and the 7th-most densely populated of the 50 United States."
stdin = sys.stdin.readlines()

# Get arguments using stdin
N = int(stdin[0])
for i in range(2*N)[1::]:
	if (i % 2) != 0:
		text = stdin[i]
		print(count_a(text))
		print(count_an(text))
		print(count_the(text))
		print(count_dates(text))