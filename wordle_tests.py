import unittest
from wordle import *

class TestWordle(unittest.TestCase):
	def test_same_word(self):
		self.assertEquals(match('words', 'words'), 'ggggg')
	
	def test_diff_word(self):
		self.assertEquals(match('orbit', 'algae'), 'bbbbb')
	
	# these two multi match tests come from
	# https://nerdschalk.com/wordle-same-letter-twice-rules-explained-how-does-it-work/
	def test_multi1(self):
		self.assertEquals(match('abbey', 'opens'), 'bbybb')
		self.assertEquals(match('abbey', 'babes'), 'yyggb')
		self.assertEquals(match('abbey', 'kebab'), 'bygyy')
		self.assertEquals(match('abbey', 'abyss'), 'ggybb')
		self.assertEquals(match('abbey', 'abbey'), 'ggggg')

	def test_multi2(self):
		self.assertEquals(match('abbey', 'algae'), 'gbbby')
		self.assertEquals(match('abbey', 'keeps'), 'bybbb')
		self.assertEquals(match('abbey', 'orbit'), 'bbgbb')
		self.assertEquals(match('abbey', 'abate'), 'ggbby')
		self.assertEquals(match('abbey', 'abbey'), 'ggggg')
