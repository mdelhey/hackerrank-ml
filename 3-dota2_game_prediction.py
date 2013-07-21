import sys
from numpy import *

txt = 'Data/dota2_train.txt'

# Train on dota2_train (n = 15,000)
train = loadtxt(txt, delimiter = ',', 
	dtype = {'names': ('hero1', 'hero2', 'hero3', 'hero4', 'hero5', 'hero6', 'hero7', 'hero8', 'hero9', 'hero10', 'outcome'),
	         'formats': ('S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'i1')})



def predict_game(heros):
	result = 1
	return(result)

stdin = sys.stdin.readlines()

# Get arguments using stdin
N = int(stdin[0])

for i in range(N):
	input = stdin[i]
	result = predict_game(input)
	print(result)