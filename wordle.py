import gzip
import json
import random
import sys


def match(known, guess):
        res = list('b'*len(known))
	known = list(known)
	# green pass
	for (i,c) in enumerate(guess):
		if c == known[i]:
			res[i] = 'g'
			known[i] = '_'
	# yellow pass
	for (i,c) in enumerate(guess):
		if res[i] != 'g' and c in known:
			res[i] = 'y'
			known[known.index(c)] = '_'
        return ''.join(res)

def trimwords(wordlist, guess, res):
	return [ w for w in wordlist if match(w, guess) == res ]


if __name__ == '__main__':
	words = json.load(gzip.open('words.json.gz'))
	while len(words) > 1:
		guess = random.choice(words)
		if len(words) < 20:
			print words
		print len(words), guess
		if len(sys.argv) > 1:
			r = match(guess, sys.argv[1])
			print r
			r = match(sys.argv[1], guess)
		else:
			r = raw_input()
		words = trimwords(words, guess, r)
	print 'answer:', words[0]


