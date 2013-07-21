import sys
import json
import itertools
import pprint

f_in  = 'Data/answered_data_10k.in'
f_out = 'Data/answered_data_10k.out'

def main():
	load_data()

def load_data():
	with open (f_in, 'r') as myfile:
		data_in = [line.replace('\n', '') for line in myfile.readlines()]
	N = int(data_in[0])
	train_in = []
	for line in data_in[1:N]:
		train_in.append(json.loads(line))
	print(train_in[u'__ans__'].values())
	
	#T = int(data_in[N + 1])
	#test_in = data_in[T+1:]


if __name__ == '__main__':
	main()