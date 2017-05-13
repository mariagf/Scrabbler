import re
import argparse
from itertools import permutations


def prefix(a):
	list = []
	datafile = file('words.txt')
	for line in datafile:
		if re.search('\A'+a, line):
			list.append(line.rstrip('\n'))
	return list;

def suffix(a):
	list = []
	datafile = file('words.txt')
	for line in datafile:
                if re.search(a+'$', line):
                    	list.append(line.rstrip('\n'))
	return list;

def find_words(a):
	list = []
	perms = [''.join(p) for p in permutations(a)]
	data = set(line.strip('\n') for line in open('words.txt'))
	for word in data.intersection(perms):
		list.append(word)
	return list;

def show(a):
	for d in a:
		print(d)
	return;

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', help='find words by prefix')
parser.add_argument('--suffix', help='find words by suffix')
parser.add_argument('word', nargs='?', default='', help='find all the possible accepted words with the letters given')

args = parser.parse_args()

if args.prefix:
	show(prefix(args.prefix))
elif args.suffix:
	show(suffix(args.suffix))
elif args.word:
	show(find_words(args.word))
