import gzip
import json
import random
import sys

# provide the comparison between a known / target word and a guess
# outputs a string with the following codes:
# b - letter is not in the word in any spot
# g - letter is in the word in the same spot
# y - letter in in the word in a different spot
# further considerations are that letters on the target word are only "used" once
# they can't both be used for g and y, for example, which is why we do two passes
def match(known, guess):
	# ugly hacks for addressable "strings"
        res = list('b'*len(known))
	known = list(known)

	# green pass
	# mark all letters in the same place
	for (i,c) in enumerate(guess):
		if c == known[i]:
			res[i] = 'g'
			known[i] = '_'

	# print ''.join(known), ''.join(res)
	
	# yellow pass
	# mark yellows and make sure to remove already used letters from target
	for (i,c) in enumerate(guess):
		if res[i] == 'g':
			continue

		if c in known:
			res[i] = 'y'
			known[known.index(c)] = '_'
	
	# print ''.join(known)

	# undo the hack
	# to those unfamiliar this creates a string by joining all the strings
	# in a list separated by ''
        return ''.join(res)

# returns a filtered wordlist with all the potential answers to a give guess
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
			r = match(sys.argv[1], guess)
			print r
		else:
			r = raw_input()
		words = trimwords(words, guess, r)
	print 'answer:', words[0]


