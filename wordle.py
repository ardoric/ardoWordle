import gzip
import json
import random
import sys


def match(known, guess):
        res = ''
        for (c1,c2) in zip(known, guess):
                if c1 == c2:
                        res += 'g'
                elif c2 in known:
                        res += 'y'
                else:
                        res += 'b'
        return res

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


